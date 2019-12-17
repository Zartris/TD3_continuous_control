import random

import torch
import torch.optim as optim

from models.model import Actor, Critic
from replay_buffers.per_nstep import PerNStep

### NOTES:
# PER           https://arxiv.org/pdf/1707.08817.pdf
# TD3 medium:   https://towardsdatascience.com/td3-learning-to-run-with-ai-40dfc512f93
# TD3 Extra:    https://spinningup.openai.com/en/latest/algorithms/td3.html#background
class TD3Agent():
    """Interacts with and learns from the environment."""

    def __init__(self, state_size, action_size, random_seed, train_num, per: bool = True):
        """Initialize an Agent object.

        Params
        ======
            state_size (int): dimension of each state
            action_size (int): dimension of each action
            random_seed (int): random seed
        """
        self.state_size = state_size
        self.action_size = action_size
        self.seed = random.seed(random_seed)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        # Actor Network (w/ Target Network)
        self.actor_local = Actor(state_size, action_size, random_seed).to(self.device)
        self.actor_target = Actor(state_size, action_size, random_seed).to(self.device)
        self.actor_optimizer = optim.Adam(self.actor_local.parameters(), lr=LR_ACTOR)

        # Critic Network (w/ Target Network)
        self.critic_local = Critic(state_size, action_size, random_seed).to(device)
        self.critic_target = Critic(state_size, action_size, random_seed).to(device)
        self.critic_optimizer = optim.Adam(self.critic_local.parameters(), lr=LR_CRITIC, weight_decay=WEIGHT_DECAY)

        # Noise process
        self.noise = OUNoise(action_size, random_seed)

        # Combined replay buffer:
        self.per = per
        if per:
            self.memory = PerNStep(BUFFER_SIZE, BATCH_SIZE, state_size, seed=random_seed, n_step=N_STEP)
        else:
            self.memory = ReplayBuffer(action_size, buffer_size=BUFFER_SIZE, batch_size=BATCH_SIZE, seed=random_seed)
        # Learning count:
        self.step_count = 0

        # Amount of training rounds:
        self.train_num = train_num

    def save(self):
        torch.save(self.actor.state_dict(), directory + 'actor.pth')
        torch.save(self.actor_target.state_dict(), directory + 'actor_target.pth')
        torch.save(self.critic_1.state_dict(), directory + 'critic_1.pth')
        torch.save(self.critic_1_target.state_dict(), directory + 'critic_1_target.pth')
        torch.save(self.critic_2.state_dict(), directory + 'critic_2.pth')
        torch.save(self.critic_2_target.state_dict(), directory + 'critic_2_target.pth')
        print("====================================")
        print("Model has been saved...")
        print("====================================")

    def load(self):
        self.actor.load_state_dict(torch.load(directory + 'actor.pth'))
        self.actor_target.load_state_dict(torch.load(directory + 'actor_target.pth'))
        self.critic_1.load_state_dict(torch.load(directory + 'critic_1.pth'))
        self.critic_1_target.load_state_dict(torch.load(directory + 'critic_1_target.pth'))
        self.critic_2.load_state_dict(torch.load(directory + 'critic_2.pth'))
        self.critic_2_target.load_state_dict(torch.load(directory + 'critic_2_target.pth'))
        print("====================================")
        print("model has been loaded...")
        print("====================================")
