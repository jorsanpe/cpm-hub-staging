import subprocess

import cpm_project_editor
from agent import Agent
import bits


BIT_USERS_DIRECTORY = 'bit_users'


class BitUserAgent(Agent):
    def __init__(self):
        super().__init__()
        self.current_state = 'idle'
        self.states = [
            'idle',
            'install_latest_bit_version',
            'install_bit_version',
            'install_non_existing_plugin',
            'install_invalid_bit_version'
        ]
        self.transition_matrix = {
            'idle': [0.8, 0.2, 0, 0, 0],
            'install_latest_bit_version': [1, 0, 0, 0, 0],
            'install_bit_version': [1, 0, 0, 0, 0],
            'install_non_existing_plugin': [1, 0, 0, 0, 0],
            'install_invalid_bit_version': [1, 0, 0, 0, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'install_latest_bit_version': self.install_latest_bit_version,
            'install_bit_version': self.install_bit_version,
            'install_non_existing_plugin': self.install_non_existing_plugin,
            'install_invalid_bit_version': self.install_invalid_bit_version,
        }
        self.project_directory = self.create_cpm_project()
        cpm_project_editor.bootstrap(self.project_directory, self.name)

    def create_cpm_project(self):
        subprocess.run(
            ['cpm', 'create', self.name],
            cwd=BIT_USERS_DIRECTORY
        )
        return f'{BIT_USERS_DIRECTORY}/{self.name}'

    def install_latest_bit_version(self):
        bit = bits.random_bit()
        subprocess.run(
            ['cpm', 'install', bit.name],
            cwd=self.project_directory
        )

    def install_bit_version(self):
        print('install_bit_version')

    def install_non_existing_plugin(self):
        print('install_non_existing_plugin')

    def install_invalid_bit_version(self):
        print('install_invalid_bit_version')

    def idle(self):
        pass
