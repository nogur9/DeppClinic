import random


class QLearningAgent:
    def __init__(self, action_space, learning_rate=0.05, epsilon=0.3):
        self.q_table = dict()  # Dictionary to store Q-values
        self.action_space = action_space
        self.learning_rate = learning_rate
        self.epsilon = epsilon

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return self.action_space.sample()  # Exploration: Random action
        else:
            return self.choose_best_action(state)  # Exploitation: Best known action

    def choose_best_action(self, state):
        state = self._format_state(state)
        if state not in self.q_table:
            return self.action_space.sample()
        max_action = -1
        max_value = -1
        for action, value in self.q_table[state].items():
            if value > max_value:
                max_value = value
                max_action = action
        return max_action

    def learn(self, state, action, reward, next_state, done=False):
        state = self._format_state(state)
        next_state = self._format_state(next_state)
        if state not in self.q_table.keys():
            possible_actions = list(range(self.action_space.n))
            self.q_table[state] = {act: 0 for act in possible_actions}

        old_value = self.q_table[state][action]

        if next_state not in self.q_table.keys():
            possible_actions = list(range(self.action_space.n))
            self.q_table[next_state] = {act: 0 for act in possible_actions}

        next_max_value = max([act_value for act_value in self.q_table[next_state].values()])

        new_value = old_value + self.learning_rate * (reward + next_max_value - old_value)

        self.q_table[state][action] = new_value

    def _format_state(self, state):
        state = state.copy()
        return tuple(state.items())

