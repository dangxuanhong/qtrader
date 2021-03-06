import numpy as np

from qtrader.agents.base import Agent


class UniformAgent(Agent):
    """Uniform agent."""

    _id = 'uniform'

    def __init__(self, action_space):
        self.N = action_space.shape[0]

    def act(self, observation):
        return np.ones(self.N) / self.N
