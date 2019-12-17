import random
import numpy as np
import torch
from replay_buffers.per_nstep import PerNStep

BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 128  # minibatch size
UPDATE_EVERY = 20

GAMMA = 0.99  # discount factor
TAU = 1e-3  # for soft update of target parameters
LR_ACTOR = 1e-4  # learning rate of the actor
LR_CRITIC = 1e-3  # learning rate of the critic
WEIGHT_DECAY = 0  # L2 weight decay


class MultiAgent():
    """Interacts with and learns from the environment."""

    def __init__(self, agents: list, seed: int, action_size, state_size):
        """wrapper for multiple agents
        Params
        ======
            agents: list of agents
        """
        self.agents = agents
        self.seed = random.seed(seed)

        # Combined replay buffer:
        self.memory = PerNStep(BUFFER_SIZE, BATCH_SIZE, state_size, seed=seed)

        # Learning count:
        self.step_count = 0

    def step(self, states, actions, rewards, next_states, dones):
        """Save experience in replay memory, and use random sample from buffer to learn."""
        self.step_count += 1
        # Save experience / reward
        for state, action, reward, next_state, done in zip(states, actions, rewards, next_states, dones):
            self.memory.add(state, action, reward, next_state, done)

        # Learn, if enough samples are available in memory
        if len(self.memory) > BATCH_SIZE:
            if self.step_count % UPDATE_EVERY == 0:
                self.step_count = 0
                self.learn()

    def act(self, states, add_noise=True):
        """Returns actions for given states as per current policy."""
        actions = []
        # select an action (for each agent)
        for agent, state in zip(self.agents, states):
            actions.append(agent.act(state))
        return np.array(actions)

    def reset(self):
        """ Reset all agent's noise """
        for agent in self.agents:
            agent.noise.reset()

    def learn(self):
        """Wrapper for learning"""
        for agent in self.agents:
            experiences = self.memory.sample()
            agent.learn(experiences, GAMMA)
