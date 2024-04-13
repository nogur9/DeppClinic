import torch
import torch.nn as nn
import torch.optim as optim


class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        # Adjust network architecture as needed based on your environment complexity
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.output = nn.Linear(32, action_size)

    def forward(self, x):
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        qvalues = self.output(x)
        return qvalues


class DQNReplayBuffer:
    def __init__(self, max_size, batch_size):
        self.max_size = max_size
        self.batch_size = batch_size
        self.states = []
        self.actions = []
        self.rewards = []
        self.next_states = []
        self.dones = []
        self.index = 0

    def push(self, state, action, reward, next_state, done):
        if len(self.states) == self.max_size:
            self.states.pop(0)
            self.actions.pop(0)
            self.rewards.pop(0)
            self.next_states.pop(0)
            self.dones.pop(0)
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.next_states.append(next_state)
        self.dones.append(done)
        self.index = (self.index + 1) % self.max_size

    def sample(self):
        if len(self.states) < self.batch_size:
            return None, None, None, None, None
        indices = np.random.choice(len(self.states), size=self.batch_size, replace=False)
        return (torch.FloatTensor(np.array(self.states)[indices])), \
               (torch.LongTensor(np.array(self.actions)[indices])), \
               (torch.FloatTensor(np.array(self.rewards)[indices])), \
               (torch.FloatTensor(np.array(self.next_states)[indices])), \
               (torch.FloatTensor(np.array(self.dones)[indices]))


class DQNLearner:
    def __init__(self, action_space, learning_rate=0.0001, gamma=0.99, eps_start=1.0, eps_end=0.01, eps_decay=0.995,
                 update_target_freq=1000):
        self.action_space = action_space
        self.state_size = self.action_space.n
        self.q_network = DQN(self.state_size, self.action_space.n)
        self.target_network = DQN(self.state_size, self.action_space.n)
        self.target_network.load_state_dict(self.q_network.state_dict())
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=learning_rate)
        self.gamma = gamma
        self.eps = eps_start
        self.eps_end = eps_end
        self.eps_decay = eps_decay
        self.update_target_freq = update_target_freq
        self.replay_buffer = DQNReplayBuffer(10000, 32)

    def choose_action(self, state):
        return self.action_space.sample()

    def choose_best_action(self, state):
        # Epsilon-greedy exploration-exploitation
        with torch.no_grad():
            state = torch.FloatTensor([state]).to(self.device)
            qvalues = self.q_network(state)
            _, action = torch.max(qvalues, dim=1)
            return action.item

    def learn(self, state, action, reward, next_state, done):
        self.replay_buffer.push(state, action, reward, next_state, done)

        # Sample a batch from the replay buffer
        states, actions, rewards, next_states, dones = self.replay_buffer.sample()
        if states is None:
            return

        # Get Q-values for current and next states
        qvalues = self.q_network(states)
        next_qvalues = self.target_network(next_states)

        # Select the action with the highest Q-value from the next state (target network)
        next_qvalues_max = next_qvalues.detach().max(dim=1, keepdim=True)[0]

        # Calculate target Q-values using Bellman equation
        target_qvalues = rewards + self.gamma * next_qvalues_max * (1 - dones)

        # Calculate loss
        loss = nn.functional.mse_loss(qvalues[range(len(states)), actions], target_qvalues)

        # Optimize the Q-network
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Update the target network regularly
        if self.t % self.update_target_freq == 0:
            self.target_network.load_state_dict(self.q_network.state_dict())

        # Decay exploration rate
        self.eps = max(self.eps_end, self.eps * self.eps_decay)
        self.t += 1

