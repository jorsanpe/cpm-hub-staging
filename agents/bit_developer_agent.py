import json
import subprocess
from http import HTTPStatus
import requests
import pexpect
import cpm_project_editor

from agent import Agent
import bits
import logger


CPM_HUB_URL = 'http://localhost:8000'
CPM_HUB_AUTH_URL = 'http://localhost:7003'


class BitDeveloperAgent(Agent):
    def __init__(self):
        super().__init__()
        self.current_state = 'idle'
        self.invitation_token = None
        self.version = '0.1'
        self.states = [
            'idle',
            'request_invitation_token',
            'register_with_valid_token',
            'idle_registered',
            'publish_plugin',
            'install_latest_bit_version',
            'add_bit_to_project',
        ]
        self.transition_matrix = {
            'idle':                         [0.95, 0.05, 0, 0, 0, 0, 0],
            'request_invitation_token':     [0, 0, 1, 0, 0, 0, 0],
            'register_with_valid_token':    [0, 0, 0, 1, 0, 0, 0],
            'idle_registered':              [0, 0, 0, 0.90, 0.09, 0.005, 0.005],
            'publish_plugin':               [0, 0, 0, 1, 0, 0, 0],
            'install_latest_bit_version':   [0, 0, 0, 1, 0, 0, 0],
            'add_bit_to_project':           [0, 0, 0, 1, 0, 0, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'request_invitation_token': self.request_invitation_token,
            'register_with_valid_token': self.register_with_valid_token,
            'idle_registered': self.idle,
            'publish_plugin': self.publish_plugin,
            'install_latest_bit_version': self.install_latest_bit_version,
            'add_bit_to_project': self.add_bit_to_project,
        }
        self.project_directory = self.create_cpm_project()
        cpm_project_editor.bootstrap(self.project_directory, self.name)

    def create_cpm_project(self):
        subprocess.run(
            ['cpm', 'create', self.name],
            cwd=bits.BIT_DEVELOPERS_DIRECTORY
        )
        return f'{bits.BIT_DEVELOPERS_DIRECTORY}/{self.name}'

    def request_invitation_token(self):
        response = requests.post(f'{CPM_HUB_AUTH_URL}/otp/{self.name}')
        if response.status_code == HTTPStatus.OK:
            self.invitation_token = response.text
        else:
            logger.message(f'BitDeveloperAgent({self.name}): FAIL request_invitation_token')
            self.current_state = 'idle'

    def register_with_valid_token(self):
        registration_date = json.dumps({
            'invitation_token': self.invitation_token,
            'username': self.name,
            'password': self.name,
            'email': self.name,
        })
        response = requests.post(f'{CPM_HUB_URL}/users', data=registration_date)
        if response.status_code == HTTPStatus.OK:
            self.invitation_token = response.text
        else:
            logger.message(f'BitDeveloperAgent({self.name}): FAIL register_with_valid_token')
            self.current_state = 'idle'

    def publish_plugin(self):
        child = pexpect.spawn(f'cpm publish -s {CPM_HUB_URL}/bits', cwd=self.project_directory)
        child.expect([pexpect.TIMEOUT, "username:"])
        child.sendline(self.name)
        child.expect([pexpect.TIMEOUT, "password:"])
        child.sendline(self.name)
        child.read()

    def install_latest_bit_version(self):
        bit = bits.random_bit()
        subprocess.run(
            ['cpm', 'install', bit.name],
            cwd=self.project_directory
        )

    def add_bit_to_project(self):
        bit = bits.random_bit()
        cpm_project_editor.add_bit(self.project_directory, bit)
        subprocess.run(
            ['cpm', 'install'],
            cwd=self.project_directory
        )

    def idle(self):
        pass
