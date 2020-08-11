# from trello.client import Client
from pathlib import Path
from os import path
import json
import requests

key = "0581b1db0a42258051a8a25fb301e247"
token = "e6985b1a4afdfb4168814ca486e76ff704e171d5751ce9db8c96731f8b1cc0cb"
# client = Client(key, token)


# home_dir = "~"
# config_file = ".ectrello-config"
# config_dir = home_dir + "/" + config_file
# config_path = Path(path.expanduser(config_dir))


class Configuration():
    def __init__(self, config_path):
        self.config_path = config_path
        self.key = None
        self.token = None

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
            print("Please enter your trello API keys:")
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
                print("Please enter your trello API keys:")
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
