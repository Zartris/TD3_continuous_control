import argparse
import os
from collections import deque
from pathlib import Path

import numpy as np
from tensorboardX import SummaryWriter
from unityagents import UnityEnvironment

from agents.td3_agent import TD3Agent


def eval_agent(brain_name, agent: TD3Agent, n_episodes=1000, max_t=1000, print_every=100):
    scores_deque = deque(maxlen=print_every)
    scores = []
    for i_episode in range(1, n_episodes + 1):
        env_info = env.reset(train_mode=True)[brain_name]  # reset the environment
        states = env_info.vector_observations  # get the current state (for each agent)
        agent.reset()  # Reset all agents
        score = np.zeros(num_agents)
        for t in range(max_t):
            actions = agent.act(states, add_noise=False)  # select an action (for each agent)
            env_info = env.step(actions)[brain_name]  # send all actions to tne environment
            next_states = env_info.vector_observations  # get next state (for each agent)
            dones = env_info.local_done  # see if episode finished
            score += env_info.rewards  # update the score (for each agent)
            states = next_states  # roll over states to next time step
            if np.any(dones):
                break
        scores_deque.append(np.mean(score))
        scores.append(np.mean(score))
        avg_score = np.mean(scores_deque)
        print('\rEpisode {}\tAverage Score: {:.2f} \t current: {:.3f}'.format(i_episode, avg_score, np.mean(score)),
              end="")
        if i_episode % print_every == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
    return scores


def train_agent(brain_name, agent: TD3Agent, n_episodes=1000, max_t=1000, print_every=100):
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
            score += env_info.rewards  # update the score (for each agent)
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
        if i_episode % print_every == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
        if avg_score > 30:
            agent.save()
            if avg_score > 30:
                print('\nEnvironment solved in {:d} episodes!'.format(i_episode))
                break

    return scores


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=0, type=int)  # The seed for testing
    parser.add_argument("--max_timesteps", default=1000, type=int)  # Max time per episode
    parser.add_argument("--episodes", default=1000, type=int)  # Number of episodes to train for
    parser.add_argument("--batch_size", default=512, type=int)  # Batch size for training
    parser.add_argument("--buffer_size", default=2 ** 20, type=int)  # Batch size for training
    parser.add_argument("--discount", default=0.99)  # Discount factor
    parser.add_argument("--tau", default=0.005)  # Soft update factor
    parser.add_argument("--lr_actor", default=1e-3)  # Optimizer learning rate for the actor
    parser.add_argument("--lr_critic", default=1e-3)  # Optimizer learning rate for the critic
    parser.add_argument("--policy_noise", default=0.2)  # Noise added to target policy during critic update
    parser.add_argument("--noise_clip", default=0.5)  # Range to clip target policy noise
    parser.add_argument("--train_delay", default=2, type=int)  # Frequency of delayed policy updates
    parser.add_argument("--save_model_path", default=os.path.join(os.getcwd(), "saved_checkpoints"))  # save dir
    parser.add_argument("--load_model_path", default="")  # If should load model: if "" don't load anything
    parser.add_argument("--eval", default=False, type=bool)  # If we only want to evaluate a model.
    parser.add_argument("--slow_and_pretty", default=False, type=bool)  # If we only want to evaluate a model.

    args = parser.parse_args()

    gamefile = Path(os.getcwd(), 'Reacher', 'Reacher.exe')
    env = UnityEnvironment(file_name=str(gamefile), seed=args.seed)
    # get the default brain
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]

    #### 2. Examine the State and Action Spaces
    # reset the environment
    env_info = env.reset(train_mode=args.slow_and_pretty)[brain_name]

    # number of agents
    num_agents = len(env_info.agents)
    print('Number of agents:', num_agents)

    # size of each action
    action_size = brain.vector_action_space_size
    action_val_high = 1
    action_val_low = -1
    print('Size of each action:', action_size)

    # examine the state space
    states = env_info.vector_observations
    state_size = states.shape[1]
    print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
    print('The state for the first agent looks like:', states[0])

    #### 3. Take Random Actions in the Environment
    scores = np.zeros(num_agents)  # initialize the score (for each agent)
    agent = TD3Agent(state_size,
                     action_size,
                     action_val_high=action_val_high,
                     action_val_low=action_val_low,
                     random_seed=args.seed,
                     train_delay=args.train_delay,
                     buffer_size=args.buffer_size,
                     batch_size=args.batch_size,
                     discount=args.discount,
                     tau=args.tau,
                     lr_actor=args.lr_actor,
                     lr_critic=args.lr_critic,
                     policy_noise=args.policy_noise,
                     noise_clip=args.noise_clip,
                     per=False,  # Not implemented yet
                     model_dir=args.load_model_path if args.eval else args.save_model_path
                     )
    agent.save()
    # Creating wrapper to handle multiple agents.
    # agent = MultiAgent(agents=agents, seed=seed, action_size=action_size, state_size=state_size)
    if not args.eval:
        scores = train_agent(brain_name=brain_name,
                             agent=agent,
                             n_episodes=args.episodes,
                             max_t=args.max_timesteps)
        print('Total score (averaged over agents) this episode: {}'.format(np.mean(scores)))
    else:
        agent.load()
        scores = eval_agent(brain_name=brain_name,
                            agent=agent,
                            n_episodes=args.episodes,
                            max_t=args.max_timesteps)
        print('Total score (averaged over agents) this episode: {}'.format(np.mean(scores)))
