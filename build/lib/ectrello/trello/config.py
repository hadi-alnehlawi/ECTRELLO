# from trello.client import Client
from pathlib import Path
from os import path
import json
import requests


class Configuration():
    def __init__(self, config_path=None, key=None, token=None):
        self.config_path = config_path
        self.key = key
        self.token = token

    def check_config(self):
        if (self.config_path.exists()):
            return True
        else:
            return False

    def get_config(self):
        if self.config_path.exists():
            with open(self.config_path, "r") as f:
                conf_dict = json.loads(f.read())
                self.key = conf_dict["key"]
                self.token = conf_dict["token"]
        else:
            return

    def overwrite_config(self):
        with open(self.config_path, "w") as f:
            # print("Please enter your trello API keys")
            self.key = input("key : ")
            self.token = input("token : ")
            conf_dict = f'{{"key": "{self.key}", "token": "{self.token}"}}'
            f.write(conf_dict)

    def post_config(self):
        conf_dict = {}
        if self.config_path.is_file():
            with open(self.config_path, "r") as f:
                conf_dict = json.loads(f.read())
                self.key = conf_dict["key"]
                self.token = conf_dict["token"]
        else:
            with open(self.config_path, "w") as f:
                # print(" enter your trello API keys")
                self.key = input("key : ")
                self.token = input("token : ")
                conf_dict = f'{{"key": "{self.key}", "token": "{self.token}"}}'
                f.write(conf_dict)

    def check_with_trello(self):
        try:
            self.get_config()
            url = f"https://api.trello.com/1/tokens/{self.token}?key={self.key}&token={self.token}"
            keys_response = requests.get(url).json()
            return True
        except:
            return False

    def check_unittest_with_trello(self):
        try:
            url = f"https://api.trello.com/1/tokens/{self.token}?key={self.key}&token={self.token}"
            keys_response = requests.get(url).json()
            return True
        except:
            return False
