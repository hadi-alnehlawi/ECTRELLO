from trello.client import Client

key = "0581b1db0a42258051a8a25fb301e247"
token = "e6985b1a4afdfb4168814ca486e76ff704e171d5751ce9db8c96731f8b1cc0cb"
client = Client(key, token)

# ****
# GET
# ****

# boards
boards = client.get_boards()
print(boards)

# board
board_id = client.get_boards()[1].id
board = client.get_board(board_id)
print(board)

# # # lists in board
board_id = client.get_boards()[1].id
lists = client.get_lists_in_board(board_id)
print(lists)
#
# # list
# list_id = lists[2].id
list = client.get_list("sdfsd")
print(list)
# #
# cards = client.get_cards_in_list(list_id)
# card_id = cards[2].id
# print(cards)
# print(card_id)
#
# card
# card_id = cards[0].id
# card = client.get_card(card_id)
# print(card)
# #
# # ****
# # POST
# # ****
#
# list
# new_list = client.post_list(name="Hello10 From Python", board_id=board_id)
# print(new_list)
# #
# Card
# new_card = client.post_card("card11", list_id)
# cards = client.get_cards_in_list(list_id)

#
# label
# new_label = client.post_label(name="label10",board_id=board_id)
# print(new_label)

#
# # epilot
# labels = client.get_labels_in_board(board_id)
# # print(labels)
#
# meeting_label = labels[0]
# label_id = meeting_label.id
# lable_card = client.post_label_card(id=label_id, card_id=card_id)
# print(meeting_label)
# card = client.post_card_comment(id=card_id,comment="comment from api")
# print(card)
