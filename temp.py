
from ectrello.trello.client import Client
from ectrello.trello.config import Configuration
import os


try:
    key = os.environ['TRELLO_KEYdd']
    token = os.environ["TRELLO_TOKEN"]
    client = Client(key=key, token=token)
    print(client.get_boards())
except:
    print("please again")


print("test")
