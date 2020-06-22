import time
import numpy

import agent_names
import logger


DELAY_BETWEEN_ACTIONS = 0.2


class Agent(object):
    def __init__(self):
        self.alive = True
        self.name = agent_names.new_agent_name()

    def next_step(self):
        next_state = numpy.random.choice(self.states, replace=True, p=self.transition_matrix[self.current_state])
        logger.message(f'{self.name}: {self.current_state} -> {next_state}')
        self.current_state = next_state
        self.entry_action[next_state]()
        time.sleep(DELAY_BETWEEN_ACTIONS)
