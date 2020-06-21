import numpy


class Agent(object):
    def next_step(self):
        next_state = numpy.random.choice(self.states, replace=True, p=self.transition_matrix[self.current_state])
        print(f'{self.current_state} -> {next_state}')
        self.current_state = next_state
        self.entry_action[next_state]()
