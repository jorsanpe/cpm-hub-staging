import threading

import bit_developer_agent
import bit_user_agent
from agent import Agent


MAX_POPULATION = 400


def agent_loop(agent):
    while agent.alive:
        agent.next_step()


class SpawningAgent(Agent):
    def __init__(self):
        super().__init__()
        self.current_state = 'idle'
        self.invitation_token = None
        self.version = '0.1'
        self.states = [
            'idle',
            'spawn_bit_user_agent',
            'spawn_bit_developer_agent',
        ]
        self.transition_matrix = {
            'idle': [0.90, 0.08, 0.02],
            'spawn_bit_user_agent': [1, 0, 0],
            'spawn_bit_developer_agent': [1, 0, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'spawn_bit_user_agent': self.spawn_bit_user_agent,
            'spawn_bit_developer_agent': self.spawn_bit_developer_agent,
        }
        self.threads = []
        self.agents = []

    def stop(self):
        for agent in self.agents:
            agent.alive = False
        for thread in self.threads:
            thread.join()

    def idle(self):
        pass

    def __current_population(self):
        return len(self.agents)

    def spawn_bit_user_agent(self):
        if self.__current_population() >= MAX_POPULATION:
            return
        agent = bit_user_agent.BitUserAgent()
        agent_thread = threading.Thread(target=agent_loop, args=(agent,))
        agent_thread.start()
        self.threads.append(agent_thread)
        self.agents.append(agent)

    def spawn_bit_developer_agent(self):
        if self.__current_population() >= MAX_POPULATION:
            return
        agent = bit_developer_agent.BitDeveloperAgent()
        agent_thread = threading.Thread(target=agent_loop, args=(agent,))
        agent_thread.start()
        self.threads.append(agent_thread)
        self.agents.append(agent)
