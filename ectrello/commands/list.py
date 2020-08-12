# import click
# from trello.client import Client
#
# key = "0581b1db0a42258051a8a25fb301e247"
# token = "e6985b1a4afdfb4168814ca486e76ff704e171d5751ce9db8c96731f8b1cc0cb"
# client = Client(key, token)
#
#
# show_help = """ \n
# TEXT=all show all list in a board.\n
# TEXT=first show first in a board.\n
# TEXT=last show last in a board.\n
# """
#
# board_id_help = """ \n
# the board id you want to show its list.
# """
#
#
# @click.command()
# @click.option("--boardid",required=True, help=board_id_help)
# @click.option("--show", required=False, help=show_help)
# def cli(show,boardid):
#     """
#     Show lists of your trello board\n
#     ex: ectrello list --boardid 5f2d9bdc021517198e990081 --show all
#     """
#     if show == "all" or show is None:
#         lists = client.get_lists_in_board(boardid)
#         print(lists)
#     elif show == "first":
#         first_list = client.get_lists_in_board(boardid)[0]
#         print(first_list)
#     elif show == "last":
#         first_list = client.get_lists_in_board(boardid)[-1]
#         print(first_list)
#     elif show == "--help":
#         print("helping")
#     else:
#         list = client.get_list(id=list,board_id=boardid)
#         print(list)
