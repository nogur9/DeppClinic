import pandas as pd

from source.projects.RL_research.agents.q_learning import QLearningAgent
from source.projects.RL_research.params import RAND_PATIENT_ID, QUESTIONS
from source.projects.RL_research.RL_utils import DiagnosticEnv


def prediction_episode(env, agent, state, done=False, verbose=False):

    while not done:
        action = agent.choose_best_action(state)  # State converted to string for simplicity
        print(f"{action = }")
        next_state, reward, done = env.step(action, eval=True)
        state = next_state.copy()
    if verbose:
        print(f"{reward = }")
    return state


def training_episode(env, agent, state, done=False):
    while not done:
        action = agent.choose_action(state)  # State converted to string for simplicity
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state, done=done)
        state = next_state.copy()
    return reward


def training_loop(env, agent, n_episodes, verbose=False):

    for _ in range(n_episodes):
        # prepare
        state = env.reset()
        done = False
        # play
        reward = training_episode(env, agent, state, done)
        if verbose and False:
            print(f"{reward = }")


def single_patient_train(patient_id, df, agent, n_episodes, verbose=False, custom_questions=None):
    if verbose:
        print(f"{patient_id = }")
    if custom_questions is None:
        questions = QUESTIONS
    else:
        questions = custom_questions
    env = DiagnosticEnv(df, patient_id=patient_id, questions=questions)
    training_loop(env, agent, n_episodes, verbose=verbose)


def train_agent(training_ids, df, n_episodes, verbose=False, custom_questions=None):
    if custom_questions is None:
        questions = QUESTIONS
    else:
        questions = custom_questions

    action_space = DiagnosticEnv(df, patient_id=RAND_PATIENT_ID,
                                 questions=questions).action_space

    # Initialize agent
    agent = QLearningAgent(action_space)

    for patient_id in training_ids:
        single_patient_train(patient_id, df, agent, n_episodes, verbose=verbose, custom_questions=custom_questions)

    return agent


def do_interview(df, agent, custom_questions=None, verbose=False):
    if custom_questions is None:
        questions = QUESTIONS
    else:
        questions = custom_questions
    interviews = []  # Collect patient info in a list
    for patient_id in df.id.unique():
        print(f"{patient_id = }")
        env = DiagnosticEnv(df, patient_id=patient_id, questions=questions)
        state = env.reset()
        patient_info = prediction_episode(env, agent, state, verbose=verbose)
        patient_info = {question: answer for question, answer in zip(questions, list(patient_info.values()))}
        patient_info['id'] = patient_id
        if 'Y' in df.columns:
            patient_info['Y'] = df.query(f'id == "{patient_id}"')['Y'].iloc[0]  # Use iloc[0] for first item
        interviews.append(patient_info)

    interview_df = pd.DataFrame(interviews)  # Convert list of dicts to DataFrame
    return interview_df
