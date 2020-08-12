
class Board():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'{{ id: {self.id}, name: {self.name} }}'


class List():
    def __init__(self, id, name, board_id=None):
        self.id = id
        self.name = name
        self.board_id = board_id

    def __repr__(self):
        return f'{{ id: {self.id}, name: {self.name} }}'


class Card():
    def __init__(self, id, name, list_id=None, comment=None, labels_id=None, board_id=None):
        self.id = id
        self.name = name
        self.list_id = list_id
        self.comment = comment
        self.labels_id = labels_id
        self.board_id = board_id

    def __repr__(self):
        return f"{{ id: {self.id}, name: {self.name}, labels_id: {self.labels_id}, comment: {self.comment} , board_id: {self.board_id} }}"


class Label():
    def __init__(self, name, id=None, card_id=None, board_id=None):
        self.name = name
        self.card_id = card_id
        self.id = id
        self.board_id = board_id

    def __repr__(self):
        if self.card_id is not None:
            return f"{{ name:{self.name}, card_id:{self.card_id} }}"
        else:
            return f"{{ name:{self.name}, board_id:{self.board_id} }}"


class Comment():
    def __init__(self, text, card_id):
        self.text = text
        self.card_id = card_id

    def __repr__(self):
        return f"{{ text: {self.text}, card_id: {self.card_id} }}"
