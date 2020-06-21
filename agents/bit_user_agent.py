import time
import subprocess

import cpm_project_editor
from agent import Agent
import bits


IDLE_TIME = 0.2
BIT_USERS_DIRECTORY = 'bit_users'


class BitUserAgent(Agent):
    def __init__(self, name):
        self.current_state = 'idle'
        self.name = name
        self.states = [
            'idle',
            'install_latest_plugin_version',
            'install_plugin_version',
            'install_non_existing_plugin',
            'install_invalid_plugin_version'
        ]
        self.transition_matrix = {
            'idle': [0.8, 0.2, 0, 0, 0],
            'install_latest_plugin_version': [1, 0, 0, 0, 0],
            'install_plugin_version': [1, 0, 0, 0, 0],
            'install_non_existing_plugin': [1, 0, 0, 0, 0],
            'install_invalid_plugin_version': [1, 0, 0, 0, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'install_latest_plugin_version': self.install_latest_plugin_version,
            'install_plugin_version': self.install_plugin_version,
            'install_non_existing_plugin': self.install_non_existing_plugin,
            'install_invalid_plugin_version': self.install_invalid_plugin_version,
        }
        self.project_directory = self.create_cpm_project()
        cpm_project_editor.bootstrap(self.project_directory, self.name)

    def create_cpm_project(self):
        subprocess.run(
            ['cpm', 'create', self.name],
            cwd=BIT_USERS_DIRECTORY
        )
        return f'{BIT_USERS_DIRECTORY}/{self.name}'

    def install_latest_plugin_version(self):
        bit = bits.random_bit()
        subprocess.run(
            ['cpm', 'install', bit],
            cwd=self.project_directory
        )

    def install_plugin_version(self):
        print('install_plugin_version')

    def install_non_existing_plugin(self):
        print('install_non_existing_plugin')

    def install_invalid_plugin_version(self):
        print('install_invalid_plugin_version')

    def idle(self):
        time.sleep(IDLE_TIME)
