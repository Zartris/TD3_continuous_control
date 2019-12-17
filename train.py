import os
from collections import deque
from pathlib import Path

import numpy as np
import torch
from unityagents import UnityEnvironment

from agents.ddpg_agent import Agent
from tensorboardX import SummaryWriter


def train_agent(brain_name, agent: Agent, n_episodes=1000, max_t=1000, print_every=100):
    writer = SummaryWriter("logging")
    scores_deque = deque(maxlen=print_every)
    scores = []
    for i_episode in range(1, n_episodes + 1):
        env_info = env.reset(train_mode=True)[brain_name]  # reset the environment
        states = env_info.vector_observations  # get the current state (for each agent)
        agent.reset()  # Reset all agents
        score = np.zeros(num_agents)
        for t in range(max_t):
            actions = agent.act(states)  # select an action (for each agent)
            env_info = env.step(actions)[brain_name]  # send all actions to tne environment
            next_states = env_info.vector_observations  # get next state (for each agent)
            rewards = env_info.rewards  # get reward (for each agent)
            dones = env_info.local_done  # see if episode finished
            agent.step(states, actions, rewards, next_states, dones)
            score += rewards  # update the score (for each agent)
            states = next_states  # roll over states to next time step
            if np.any(dones):
                break
        scores_deque.append(np.mean(score))
        scores.append(np.mean(score))
        writer.add_scalar('score_per_episode', np.mean(score), i_episode - 1)
        avg_score = np.mean(scores_deque)
        writer.add_scalar('score_avg_over_100_episodes', avg_score, i_episode - 1)
        print('\rEpisode {}\tAverage Score: {:.2f} \t current: {:.3f}'.format(i_episode, avg_score, np.mean(score)),
              end="")

        # torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
        # torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')
        if i_episode % print_every == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
        if avg_score > 30:
            if avg_score > 30:
                print('\nEnvironment solved in {:d} episodes!'.format(i_episode))
                break

    return scores


if __name__ == '__main__':
    seed = 0
    gamefile = Path(os.getcwd(), 'Reacher', 'Reacher.x86_64')
    env = UnityEnvironment(file_name=str(gamefile), seed=seed)
    # get the default brain
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]

    #### 2. Examine the State and Action Spaces
    # reset the environment
    env_info = env.reset(train_mode=True)[brain_name]

    # number of agents
    num_agents = len(env_info.agents)
    print('Number of agents:', num_agents)

    # size of each action
    action_size = brain.vector_action_space_size
    print('Size of each action:', action_size)

    # examine the state space
    states = env_info.vector_observations
    state_size = states.shape[1]
    print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
    print('The state for the first agent looks like:', states[0])

    #### 3. Take Random Actions in the Environment
    scores = np.zeros(num_agents)  # initialize the score (for each agent)
    agent = Agent(state_size, action_size, random_seed=0, train_num=10, per=True)
    # Creating wrapper to handle multiple agents.
    # agent = MultiAgent(agents=agents, seed=seed, action_size=action_size, state_size=state_size)
    scores = train_agent(brain_name, agent)
    print('Total score (averaged over agents) this episode: {}'.format(np.mean(scores)))
