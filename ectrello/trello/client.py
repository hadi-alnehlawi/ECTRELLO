import requests
import json
from .model import Board, List, Card, Label
from .api import TrelloAPI


class Client():
    def __init__(self, key, token):
        self.key = key
        self.token = token
        request_query = f"key={self.key}" + "&" + f"token={self.token}"
        self.trello_api = TrelloAPI(request_query)
    # ******
    # BOARD
    # ******

    def get_boards(self):
        boards = []
        url = self.trello_api.boards_url()
        boards_response = requests.get(url).json()
        for board_dict in boards_response:
            id = board_dict.get("id")
            name = board_dict.get("name")
            boards.append(Board(id, name))
        return boards

    def get_boards_id(self):
        boards_id = [board.id for board in self.get_boards()]
        return boards_id

    def get_board(self, id):
        if not id in self.get_boards_id():
            return {"status_code": 404, "message": f"[{board_id}] is not an existing id"}
        else:
            url = self.trello_api.board_url(id)
            board_response = requests.get(url).json()
            id = board_response.get("id")
            name = board_response.get("name")
            return Board(id, name)
    # ******
    # LIST
    # ******

    def get_lists_in_board(self, board_id):
        lists = []
        if not board_id in self.get_boards_id():
            return {"status_code": 404, "message": f"[{board_id}] is not an existing id"}
        else:
            url = self.trello_api.lists_in_board_url(board_id)
            lists_response = requests.get(url).json()
            for list_dict in lists_response:
                id = list_dict.get("id")
                name = list_dict.get("name")
                lists.append(List(id=id, name=name, board_id=board_id))
            return lists

    def get_list(self, id):
        try:
            url = self.trello_api.list_url(id=id, method="GET")
            list_response = requests.get(url).json()
            id = list_response.get("id")
            name = list_response.get("name")
            return List(id, name)
        except:
            return {"status_code": requests.get(url).status_code, "message": f"[{list_id}] is not an existing id"}

    def post_list(self, name, board_id):
        try:
            payload = {
                "key": f"{self.key}", "token": f"{self.token}", "name": f"{name}", "idBoard": f"{board_id}"
            }
            url = self.trello_api.list_url(method="POST")
            list_response = requests.post(url=url, json=payload)
            res_json = json.loads(list_response.text)
            id = res_json.get("id")
            name = res_json.get("name")
            return List(id=id, name=name, board_id=board_id)
        except:
            return {"status_code": requests.get(url).status_code, "message": f"[{board_id}] is not an existing id"}

    # *****
    # CARD
    # *****

    def get_cards_in_list(self, list_id):
        try:
            cards = []
            url = self.trello_api.cards_in_list_url(list_id)
            cards_in_list_response = requests.get(url).json()
            for card_dict in cards_in_list_response:
                id = card_dict.get("id")
                name = card_dict.get("name")
                cards.append(Card(id, name, list_id))
            return cards
        except:
            return {"status_code": requests.get(url).status_code, "message": f"[{list_id}] is not an existing id"}

    def get_card(self, id):
        try:
            url = self.trello_api.card_url(id=id, method="GET")
            card_response = requests.get(url).json()
            id = card_response.get("id")
            name = card_response.get("name")
            return Card(id, name)
        except:
            return {"status_code": requests.get(url).status_code, "message": f"[{id}] is not an existing id"}

    def post_card(self, name, list_id):
        try:
            payload = {
                "key": f"{self.key}", "token": f"{self.token}", "name": f"{name}", "idList": f"{list_id}"
            }
            url = self.trello_api.card_url(method="POST")
            card_response = requests.post(url=url, json=payload)
            res_json = json.loads(card_response.text)
            id = res_json.get("id")
            name = res_json.get("name")
            return Card(id=id, name=name, list_id=list_id)
        except:
            return {"status_code": requests.get(url).status_code, "message": f"[{list_id}] is not existed id"}

    # add comment to a card
    def post_card_comment(self, id, comment):
        payload = {
            "key": f"{self.key}", "token": f"{self.token}", "id": f"{id}", "text": f"{comment}"
        }
        url = self.trello_api.card_comment_url(id)
        card_comment_response = requests.post(url=url, json=payload)
        if card_comment_response.status_code == 200:
            res_json = json.loads(card_comment_response.text)
            id = res_json.get("id")
            name = res_json.get("name")
            comment = res_json.get("data").get("text")
            print(comment)
            return Card(id=id, name=name, comment=comment)
        else:
            return card_comment_response.status_code

    # *****
    # LABEL
    # *****
    def get_labels_in_board(self, board_id):
        labels = []
        if not board_id in self.get_boards_id():
            return {"status": 404, "message": "board_id is not valid"}
        else:
            url = self.trello_api.labels_in_board_url(board_id)
            lists_response = requests.get(url).json()
            # lists_json = self.trello_api.lists_in_board_json(board_id)
            for list_dict in lists_response:
                id = list_dict.get("id")
                name = list_dict.get("name")
                labels.append(Label(id=id, name=name, board_id=board_id))
            return labels

    def get_label(self, label_id):
        url = self.trello_api.label_url(id=id, method="GET")
        label_response = requests.get(url).json()
        id = label_responsene.get("id")
        name = label_responsene.get("id")
        return Label(id=id, name=name)

    def post_label(self, name, board_id):
        payload = {
            "key": f"{self.key}", "token": f"{self.token}", "name": f"{name}", "idBoard": f"{board_id}"
        }
        url = self.trello_api.label_url(method="POST")
        lable_response = requests.post(url=url, json=payload)
        if lable_response.status_code == 200:
            res_json = json.loads(lable_response.text)
            id = res_json.get("id")
            name = res_json.get("name")
            return Label(id=id, name=name, board_id=board_id)
        else:
            return label.response.status_code

    def post_label_card(self, id, card_id):
        payload = {
            "key": f"{self.key}", "token": f"{self.token}", "id": f"{card_id}", "value": f"{id}"
        }
        url = self.trello_api.label_card_url(card_id=card_id)
        label_card_response = requests.post(url=url, json=payload)
        if label_card_response.status_code == 200:
            res_json = json.loads(label_card_response.text)
            print(res_json)
            return "Done"
        else:
            return card_comment_response.status_code
