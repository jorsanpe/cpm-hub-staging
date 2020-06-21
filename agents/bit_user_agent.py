import time
import names
import subprocess

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
            'download_latest_plugin_version',
            'download_plugin_version',
            'download_non_existing_plugin',
            'download_invalid_plugin_version'
        ]
        self.transition_matrix = {
            'idle': [0.8, 0.2, 0, 0, 0],
            'download_latest_plugin_version': [1, 0, 0, 0, 0],
            'download_plugin_version': [1, 0, 0, 0, 0],
            'download_non_existing_plugin': [1, 0, 0, 0, 0],
            'download_invalid_plugin_version': [1, 0, 0, 0, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'download_latest_plugin_version': self.download_latest_plugin_version,
            'download_plugin_version': self.download_plugin_version,
            'download_non_existing_plugin': self.download_non_existing_plugin,
            'download_invalid_plugin_version': self.download_invalid_plugin_version,
        }
        self.create_cpm_project()

    def create_cpm_project(self):
        subprocess.run(
            ['cpm', 'create', self.name],
            cwd=BIT_USERS_DIRECTORY
        )

    def download_latest_plugin_version(self):
        bit = bits.random_bit()
        print('download_latest_plugin_version')

    def download_plugin_version(self):
        print('download_plugin_version')

    def download_non_existing_plugin(self):
        print('download_non_existing_plugin')

    def download_invalid_plugin_version(self):
        print('download_invalid_plugin_version')

    def idle(self):
        time.sleep(IDLE_TIME)
