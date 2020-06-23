#!/usr/bin/env python3
import threading
import time

import spawning_agent


def simulation_loop(agent):
    while agent.alive:
        agent.next_step()


def run_simulation(duration=10, num_bit_developers=1, num_bit_users=1, ):
    agent = spawning_agent.SpawningAgent()
    simulation_agent = threading.Thread(target=simulation_loop, args=(agent,))
    simulation_agent.start()
    time.sleep(duration)
    agent.alive = False
    simulation_agent.join()
    agent.stop()


run_simulation(duration=120)
