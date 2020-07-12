#!/usr/bin/env python3
import threading
import time
from pathlib import Path
import shutil

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


home = str(Path.home())
local_cpm_config_file = f'{home}/.cpm.yaml'

try:
    shutil.copy2(local_cpm_config_file, 'cpm.yaml.bak')
except:
    pass

shutil.copy2('cpm.yaml.staging', local_cpm_config_file)

run_simulation(duration=600)

try:
    shutil.copy2('cpm.yaml.bak', local_cpm_config_file)
except:
    pass
