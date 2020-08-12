import unittest
import os
import json
import requests
from pathlib import Path
from os import path
from random import randint
from ectrello.trello.client import Client
from ectrello.trello.config import Configuration
from ectrello.trello.model import Board, List, Card
from ectrello.trello.config import Configuration


path = Path(path.expanduser("~/.ectrello-config"))


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board_name = f"test_board_{randint(1000000, 9999999)}"
        self.board_id = None
        self.execute_tear_down = True
        self.configuration = Configuration(config_path=path)
        try:
            if self.configuration.check_with_trello():
                pass
            else:
                raise EnvironmentError
        except EnvironmentError:
            print("Trello API's keys are not correct. Run this commnad first $ectroll configure")
            self.execute_tear_down = False
        finally:
            self.config = Configuration(key=self.configuration.key,
                                        token=self.configuration.token)

    def tearDown(self):
        if self.execute_tear_down:
            self.delete_board()

    # Add a list to a board
    def test_add_list(self):
        if self.config.check_unittest_with_trello():
            client = Client(key=self.config.key, token=self.config.token)
            new_board = self.new_board(name=self.board_name)
            list_name = f"test_list_{randint(1000000, 9999999)}"
            new_list = client.post_list(name=list_name, board_id=new_board.id)
            get_list = client.get_list(new_list.id)
            self.assertEqual(new_list.id, get_list.id)

    # Add a card to a column
    def test_add_card(self):
        if self.config.check_unittest_with_trello():
            client = Client(key=self.config.key, token=self.config.token)
            new_board = self.new_board(name=self.board_name)
            list_name = f"test_list_{randint(1000000, 9999999)}"
            new_list = client.post_list(name=list_name, board_id=new_board.id)
            new_card_name = f"test_card_{randint(1000000, 9999999)}"
            new_card = client.post_card(name=new_card_name, list_id=new_list.id)
            get_card = client.get_card(id=new_card.id)
            self.assertEqual(new_card.id, get_card.id)

    # Add a label to a card
    def test_add_label(self):
        if self.config.check_unittest_with_trello():
            client = Client(key=self.config.key, token=self.config.token)
            new_board = self.new_board(name=self.board_name)
            list_name = f"test_list_{randint(1000000, 9999999)}"
            new_list = client.post_list(name=list_name, board_id=new_board.id)
            new_card_name = f"test_card_{randint(1000000, 9999999)}"
            new_card = client.post_card(name=new_card_name, list_id=new_list.id)
            new_label_name = f"test_label_{randint(1000000, 9999999)}"
            new_label = client.post_label_to_baord(name=new_label_name, board_id=new_board.id)
            new_label_card = client.post_label_to_card(id=new_label.id, card_id=new_card.id)
            get_label = client.get_label(id=new_label.id)
            self.assertEqual(new_label.id, get_label.id)

    # Add a comment to a card
    def test_add_comment(self):
        if self.config.check_unittest_with_trello():
            client = Client(key=self.config.key, token=self.config.token)
            new_board = self.new_board(name=self.board_name)
            list_name = f"test_list_{randint(1000000, 9999999)}"
            new_list = client.post_list(name=list_name, board_id=new_board.id)
            new_card_name = f"test_card_{randint(1000000, 9999999)}"
            new_card = client.post_card(name=new_card_name, list_id=new_list.id)
            new_comment_text = f"test_comment_{randint(1000000, 9999999)}"
            new_comment = client.post_comment_card(text=new_comment_text, card_id=new_card.id)
            get_comment = client.get_comments_in_card(card_id=new_card.id)
            # return list of comments from trello API | as we added single comment to single card_dict
            # filter on first item would be adequate
            self.assertEqual(new_comment.text, get_comment[0].text)

    def new_board(self, name):
        new_board_name = name
        url = "https://api.trello.com/1/boards/"

        query = {
            'key': {self.config.key},
            'token': {self.config.token},
            'name': new_board_name
        }
        response = json.loads((requests.request("POST", url, params=query)).text)
        board_id = response.get("id")
        board_name = response.get("name")
        self.board_id = response.get("id")
        return Board(id=board_id, name=board_name)

    def delete_board(self):
        new_board_name = self.board_name
        url = f"https://api.trello.com/1/boards/{self.board_id}"
        query = {
            'key': {self.config.key},
            'token': {self.config.token},
        }
        response = json.loads((requests.request('DELETE', url, params=query)).text)
        board_id = response.get("id")
        board_name = response.get("name")
        return Board(id=response.get("id"), name=response.get("name"))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    unittest.TextTestRunner(verbosity=2).run(suite)
