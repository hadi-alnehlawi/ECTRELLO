# import click
# from trello.client import Client
#
# key = "0581b1db0a42258051a8a25fb301e247"
# token = "e6985b1a4afdfb4168814ca486e76ff704e171d5751ce9db8c96731f8b1cc0cb"
# client = Client(key, token)
#
#
# show_help = """ \n
# TEXT=all show all boards.\n
# TEXT=first show first board.\n
# TEXT=last show last board.\n
# """
#
#
# @click.command()
# @click.option("--show", required=False, help=show_help)
# def cli(show):
#     """
#     Show board of your trello\n
#     ex: trellocli board --show all
#     """
#     if show == "all" or show is None:
#         boards = client.get_boards()
#         print(boards)
#     elif show == "first":
#         boards = client.get_boards()
#         board = client.get_board(id=boards[0].id)
#         print(board)
#     elif show == "last":
#         boards = client.get_boards()
#         board = client.get_board(id=boards[-1].id)
#         print(board)
#     elif show == "--help":
#         print("helping ")
#     else:
#         board = client.get_board(id=show)
#         print(board)
