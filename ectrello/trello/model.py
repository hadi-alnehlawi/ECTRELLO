
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
    def __init__(self, id, name, list_id=None, comment=None, labels=None):
        self.id = id
        self.name = name
        self.list_id = list_id
        self.comment = comment
        self.labels = labels

    def __repr__(self):
        return f"{{ id: {self.id}, name: {self.name}, labels: {self.labels}, comment: {self.comment} }}"


class Label():
    def __init__(self, id, name, board_id):
        self.id = id
        self.name = name
        self.board_id = board_id

    def __repr__(self):
        return f"{{ id:{self.id}, name:{self.name} }}"


class Comment():
    def __init__(self, text, card_id):
        self.text = text
        self.card_id = card_id

    def __repr__(self):
        return f"{{ text: {self.text}, card_id: {self.card_id} }}"
