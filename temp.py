from pathlib import Path
from os import path
from ectrello.trello.config import Configuration


path = Path(path.expanduser("~/.ectrello-config"))
configuration = Configuration(config_path=path)


if configuration.check_with_trello():
    print("success")
else:
    print("Trello API's keys are not correct. Run this commnad first $ectroll configure")
