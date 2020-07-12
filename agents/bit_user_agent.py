import subprocess

import cpm_project_editor
from agent import Agent
import bits
import requests


BIT_USERS_DIRECTORY = 'bit_users'


class BitUserAgent(Agent):
    def __init__(self):
        super().__init__()
        self.current_state = 'idle'
        self.states = [
            'idle',
            'install_latest_bit_version',
            'install_bit_version',
            'install_non_existing_bit',
            'install_invalid_bit_version',
            'search_for_bits'
        ]
        self.transition_matrix = {
            'idle': [0.8, 0.15, 0, 0, 0, 0.05],
            'install_latest_bit_version': [1, 0, 0, 0, 0, 0],
            'install_bit_version': [1, 0, 0, 0, 0, 0],
            'install_non_existing_bit': [1, 0, 0, 0, 0, 0],
            'install_invalid_bit_version': [1, 0, 0, 0, 0, 0],
            'search_for_bits': [1, 0, 0, 0, 0, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'install_latest_bit_version': self.install_latest_bit_version,
            'install_bit_version': self.install_bit_version,
            'install_non_existing_bit': self.install_non_existing_bit,
            'install_invalid_bit_version': self.install_invalid_bit_version,
            'search_for_bits': self.search_for_bits,
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
        result = subprocess.run(
            ['cpm', 'install', bit.name],
            cwd=self.project_directory
        )
        if result.returncode != 0:
            raise RuntimeError('failed installing latest bit version')
    
    def search_for_bits(self):
        bit = bits.random_bit()
        search_query = {
            'name': bit.name[:-3]
        }
        result = requests.get('http://127.0.0.1:8000/bits', params=search_query)
        if result.status_code != 200:
            raise RuntimeError('failed searching for bit')

    def install_bit_version(self):
        print('install_bit_version')

    def install_non_existing_bit(self):
        print('install_non_existing_bit')

    def install_invalid_bit_version(self):
        print('install_invalid_bit_version')

    def idle(self):
        pass
