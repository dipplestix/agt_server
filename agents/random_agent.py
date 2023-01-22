import random
from agent import Agent
import sys


class RandomAgent(Agent):
    def __init__(self, name):
        super(RandomAgent, self).__init__(name)
        self.history = []

    def get_action(self):
        action = random.choice(['rock', 'paper', 'scissors'])
        return action

    def update(self, a_other, utility):
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Please only enter the name of the agent')
        sys.exit()

    agent = RandomAgent(sys.argv[1])
    agent.connect(ip='127.0.1.1', port=1234)
