import json
import time
import subprocess
from http import HTTPStatus
import requests
import pexpect
from subprocess import Popen, PIPE

from agent import Agent
import logger
import bits


IDLE_TIME = 0.2
BIT_USERS_DIRECTORY = 'bit_developers'
CPM_HUB_URL = 'http://localhost:8000'
CPM_HUB_AUTH_URL = 'http://localhost:7003'


class BitDeveloperAgent(Agent):
    def __init__(self, name):
        self.current_state = 'idle'
        self.name = name
        self.invitation_token = None
        self.version = '0.1'
        self.states = [
            'idle',
            'request_invitation_token',
            'register_with_valid_token',
            'idle_registered',
            'publish_plugin',
        ]
        self.transition_matrix = {
            'idle': [0.9, 0.1, 0, 0, 0],
            'request_invitation_token': [0, 0, 1, 0, 0],
            'register_with_valid_token': [0, 0, 0, 1, 0],
            'idle_registered': [0, 0, 0, 0.90, 0.1],
            'publish_plugin': [0, 0, 0, 1, 0],
        }
        self.entry_action = {
            'idle': self.idle,
            'request_invitation_token': self.request_invitation_token,
            'register_with_valid_token': self.register_with_valid_token,
            'idle_registered': self.idle,
            'publish_plugin': self.publish_plugin,
        }
        self.project_directory = self.create_cpm_project()

    def create_cpm_project(self):
        subprocess.run(
            ['cpm', 'create', self.name],
            cwd=BIT_USERS_DIRECTORY
        )
        return f'{BIT_USERS_DIRECTORY}/{self.name}'

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
        # publish_process = Popen(['cpm', 'publish', '-s', f'{CPM_HUB_URL}/bits'], stdin=PIPE, stdout=PIPE)
        # publish_process.stdin.write(f'{self.name}\n'.encode())
        # publish_process.stdin.write(f'{self.name}\n'.encode())
        # publish_process.communicate()
        # publish_process.stdin.close()
        bits.add_bit(bits.Bit(self.name, self.version))

    def idle(self):
        time.sleep(IDLE_TIME)
