
# GET
# ****

# boards
# boards = client.get_boards()
# print(boards)

# board
# board_id = client.get_boards()[1].id
# board = client.get_board(board_id)
# print(board)

# # # lists in board
# board_id = client.get_boards()[1].id
# lists = client.get_lists_in_board(board_id)
# print(lists)
#
# # list
# list_id = lists[5].id
# list = client.get_list(list_id)
# print(list)
# #
# # cards = client.get_cards_in_list(list_id)
# # card_id = cards[0].id
# card = client.get_card("5f2c3a83bba30c06ba1bcbe2")
# print("card ", card)
#
# # comment


# new_comment = client.post_comment_card(card_id=card_id, text="new comment 12:120 am")
# comment = client.get_comments_in_card("5f2c3a83bba30c06ba1bcbe2")
# print(comment)
# print(comment)
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
# # label
# label = client.get_label(id="5f2c3a817669b225490a7168")
# print("label ", label)
#
# # post_label_card = client.post_label_card(id="5f2c3a817669b225490a7168",
# #                                     card_id="5f2c3a83bba30c06ba1bcbe2")
# labels_on_card = client.get_labels_on_card(card.id)
# print("label on card", labels_on_card)
# #
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
