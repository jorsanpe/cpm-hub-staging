#!/usr/bin/env python3
import threading
import time

import bit_developer_agent
import bit_user_agent
import agent_names

simulation_running = True


def bit_developer_function(name):
    global simulation_running
    bit_developer = bit_developer_agent.BitDeveloperAgent(name)
    while simulation_running:
        bit_developer.next_step()


def bit_user_function(name):
    global simulation_running
    bit_user = bit_user_agent.BitUserAgent(name)
    while simulation_running:
        bit_user.next_step()


def run_simulation(num_bit_developers=1, num_bit_users=1, duration=10):
    threads = []
    global simulation_running

    for i in range(num_bit_developers):
        name = agent_names.new_agent_name()
        developer = threading.Thread(target=bit_developer_function, args=(name,))
        developer.start()
        threads.append(developer)

    for i in range(num_bit_users):
        name = agent_names.new_agent_name()
        user = threading.Thread(target=bit_user_function, args=(name,))
        user.start()
        threads.append(user)

    time.sleep(duration)

    simulation_running = False

    for thread in threads:
        thread.join()


run_simulation(num_bit_developers=5, num_bit_users=10, duration=60)
