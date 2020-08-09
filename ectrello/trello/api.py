import requests


class TrelloAPI():

    def __init__(self, request_query, trello_url="https://api.trello.com/1/"):
        self.request_query = request_query
        self.trello_url = trello_url
    # Board

    def boards_url(self):
        # https://api.trello.com/1/members/me/boards?fields=name&key={{key}}&token={{token}}
        # {name} is explicity mention as {id} is always implicitly returned
        field_arg = "fields=name"
        boards_url = "members/me/boards?" + field_arg + "&" + self.request_query
        url = self.trello_url + boards_url
        return url

    def board_url(self, id):
        # https://api.trello.com/1/boards/{{boardId}}?key={{key}}&token={{token}}
        url = self.trello_url + f"boards/{id}?" + self.request_query
        return url

    # List
    def lists_in_board_url(self, board_id):
        # https://api.trello.com/1/boards/{{boardId}}/lists?key={{key}}&token={{token}}
        url = self.trello_url + f"boards/{board_id}/lists?" + self.request_query
        return url

    def list_url(self, id=None, method="GET"):
        if method == "POST":
            # https://api.trello.com/1/lists
            url = self.trello_url + f"lists"
            return url
        else:
            # https://api.trello.com/1/lists/{{listId}}?key={{key}}&token={{token}}
            url = self.trello_url + f"lists/{id}?" + self.request_query
            return url

    # Card
    def cards_in_list_url(self, list_id):
        # https://api.trello.com/1/lists/{id}/cards?key={{key}}&token={{token}}'
        url = self.trello_url + f"lists/{list_id}/cards?" + self.request_query
        return url

    def card_url(self, id=None, method="GET"):
        if method == "POST":
            # https://api.trello.com/1/cards
            url = self.trello_url + f"cards"
            return url
        else:
            # https://api.trello.com/1/cards/{{cardId}}?key={{key}}&token={{token}}
            url = self.trello_url + f"cards/{id}?" + self.request_query
            return url

    def card_comment_url(self, id):
        # https://api.trello.com/1/cards/{{cardId}}/actions/comments
        url = self.trello_url + f"cards/{id}/actions/comments"
        return url

    # Label
    def labels_in_board_url(self, board_id):
        # https://api.trello.com/1/boards/{id}/labels?key={{key}}&token={{token}}
        url = self.trello_url + f"boards/{board_id}/labels?" + self.request_query
        return url

    def label_url(self, id=None, method="GET"):
        if method == "POST":
            # https://api.trello.com/1/labels
            url = self.trello_url + f"labels"
            return url
        elif method == "PUT":
            # PUT
            # https://api.trello.com/1/labels/{id}
            url = self.trello_url + f"labels/{id}"
            return url
        else:
            # GET
            # https://api.trello.com/1/labels/{{labelId}}?key={{key}}&token={{token}}
            url = self.trello_url + f"labels/{id}"
            return url

    def label_card_url(self, card_id):
        # https://api.trello.com/1/cards/{id}/idLabels
        url = self.trello_url + f"cards/{card_id}/idLabels"
        return url
