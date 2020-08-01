import requests
import xmltodict
import json
import sys

XLD_BASE_URL = 'http://127.0.0.1:4516/deployit/repository/ci/'
REPO_ID = 'Applications/'
AUTH = ('admin', 'password')
HEADERS = {'Content-Type': 'application/json'}


class XldRepo:
    def __init__(self, repo_id, host_type=None, address=None, host_os=None, host_username=None, host_password=None,
                 host_sudo_username=None, host_port=None):
        self.repo_id = repo_id
        self.host_type = host_type
        self.host_address = address
        self.host_os = host_os
        self.host_username = host_username
        self.host_password = host_password
        self.host_sudo_username = host_sudo_username
        self.host_port = host_port

    def check_repository(self):
        repo_exists = False
        r = requests.get(XLD_BASE_URL + self.repo_id, auth=AUTH, headers=HEADERS, verify=False)
        if r.status_code == 200:
            repo_exists = True
        return repo_exists

    def get_repository_infos(self):
        r = requests.get(XLD_BASE_URL + self.repo_id, auth=AUTH, headers=HEADERS, verify=False)
        return r.content

    def create_repository(self,
                          host_type,
                          host_os,
                          host_address,
                          host_port=None,
                          host_username=None,
                          host_password=None,
                          host_sudo_username=None):
        payload = {
            "type": host_type,
            "address": host_address,
            "os": host_os,
            "port": host_port,
            "username": host_username,
            "password": host_password,
            "sudoUsername": host_sudo_username,
            "id": self.repo_id
        }
        params = json.dumps(payload)
        r = requests.request('POST', XLD_BASE_URL + self.repo_id, data=params, auth=AUTH, headers=HEADERS, verify=False)
        if 'exists' in r.content:
            r = requests.request('PUT', XLD_BASE_URL + self.repo_id, data=params, auth=AUTH, headers=HEADERS,
                                 verify=False)
        return r.content
