import pandas as pd
from source.projects.RL_research.params import RAND_PATIENT_ID, QUESTIONS
from source.projects.RL_research.RL_utils import DiagnosticEnv, DQNLearner


def prediction_episode(env, agent, state, done=False):

    while not done:
        action = agent.choose_best_action(str(state))  # State converted to string for simplicity
        next_state, reward, done = env.step(action)
        state = next_state
    return state


def training_episode(env, agent, state, done=False):
    while not done:
        action = agent.choose_action(str(state))  # State converted to string for simplicity
        print(f"{action = }")
        next_state, reward, done = env.step(action)
        agent.learn(list(state.values()), action, reward, list(next_state.values()), done=done)
        state = next_state


def training_loop(env, agent, n_episodes):
    for _ in range(n_episodes):
        # prepare
        state = env.reset()
        done = False
        # play
        training_episode(env, agent, state, done)


def single_patient_train(patient_id, df, agent, n_episodes):

    env = DiagnosticEnv(df, patient_id=patient_id, questions=QUESTIONS)
    training_loop(env, agent, n_episodes)


def train_agent(training_ids, df, n_episodes):
    # Set up environment (assuming env is your DiagnosticEnv instance)
    action_space = DiagnosticEnv(df, patient_id=RAND_PATIENT_ID,
                                 questions=QUESTIONS).action_space

    # Initialize agent
    agent = DQNLearner(action_space)

    for patient_id in training_ids:
        single_patient_train(patient_id, df, agent, n_episodes)

    return agent


def do_interview(df, agent):
    interview_df = pd.DataFrame(columns=QUESTIONS + ['id', 'Y'])
    for patient_id in df.id:
        env = DiagnosticEnv(df, patient_id=patient_id, questions=QUESTIONS)
        state = env.reset()
        patient_info = prediction_episode(env, agent, state, done=False)
        patient_info = {question: i for question, i in zip(QUESTIONS, list(patient_info))}
        patient_info['id'] = patient_id
        patient_info['Y'] = df.query(f'id == {patient_id}')['Y'].first()
        interview_df.append(patient_info)

    return interview_df

