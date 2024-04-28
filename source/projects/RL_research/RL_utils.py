from gym import spaces
import gym
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import average_precision_score

from source.projects.RL_research.params import MAX_QUESTIONS


class DiagnosticEnv(gym.Env):
    def __init__(self, df, patient_id, questions, max_questions=MAX_QUESTIONS):
        super(DiagnosticEnv, self).__init__()

        self.df = df
        self.patient_id = patient_id
        self.max_questions = max_questions

        # Define action and observation space
        self.question_list = questions
        self.action_space = spaces.Discrete(len(self.question_list))

        # Assuming answers are discrete choices, modify as needed
        self.observation_space = spaces.Dict({question: spaces.Discrete(5) for question in self.question_list})
        self.state = np.nan
        self.reset()

    def reset(self):
        self.state = {question: np.nan for question in self.question_list}
        self.counter = 0
        return self.state.copy()

    def step(self, action, eval=False):
        question = self.question_list[action]
        answer = self.get_value(question) > 0
        self.state[question] = answer

        self.counter += 1
        is_done = self.counter == self.max_questions
        if is_done and (not eval):
            reward = self.calculate_reward()
        else:
            reward = 0

        return self.state, reward, is_done

    def get_value(self, question):
        value = self.df.query("id == @self.patient_id")[question].iloc[0]
        return value

    def calculate_reward(self):

        X, Y, x_test, y_test = self._prepare_test_set()
        clf = RandomForestClassifier(class_weight='balanced')
        clf.fit(X, Y)
        y_pred = clf.predict_proba(x_test)
        pr_auc = average_precision_score(y_test, y_pred[:, 1])
        return pr_auc

    def _prepare_test_set(self):

        test_set_ids = self._create_test_set_ids()

        test_df = self.df[self.df.id.isin(test_set_ids)]
        training_df = self.df[~self.df.id.isin(test_set_ids)]

        X, Y, x_test, y_test = self.create_y(training_df, test_df)
        return X, Y, x_test, y_test

    def _create_test_set_ids(self):
        df_without_patient = self.df.query("id != @self.patient_id")
        pos_samples = df_without_patient.query("Y == 1")
        neg_samples = df_without_patient.query("Y == 0")

        pos_samples = list(pos_samples.id.sample(1))
        neg_samples = list(neg_samples.id.sample(9))

        test_set_ids = pos_samples + neg_samples + [self.patient_id]
        return test_set_ids

    def create_y(self, training_df, test_df):
        X_cols = []
        for k, v in self.state.items():
            if not np.isnan(v):
                X_cols.append(k)
        Y = training_df['Y']
        X = training_df[X_cols]
        x_test = test_df[X_cols]
        y_test = test_df['Y']

        return X, Y.astype(int), x_test, y_test.astype(int)

