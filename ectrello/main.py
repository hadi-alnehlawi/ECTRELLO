import click
from .trello.client import Client

key = "0581b1db0a42258051a8a25fb301e247"
token = "e6985b1a4afdfb4168814ca486e76ff704e171d5751ce9db8c96731f8b1cc0cb"
client = Client(key, token)


class Format:
    end = '\033[0m'
    underline = '\033[4m'


def underline(str):
    return Format.underline + str + Format.end


def docstring_parameter(*sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj
    return dec


@click.group()
def cli():
    pass


show_help_board = """ \n
TEXT=all show all boards.\n
TEXT=first show first board.\n
TEXT=last show last board.\n
"""

show_board_ex_help = underline("ectrello board") + " " + "--show all"


@cli.command('board')
@click.option("--show", required=False, help=show_help_board)
@docstring_parameter(show_board_ex_help)
def board(show):
    """
    Show board of your trello\n
    ex: {0}
    """
    if show == "all" or show is None:
        boards = client.get_boards()
        print(boards)
    elif show == "first":
        boards = client.get_boards()
        board = client.get_board(id=boards[0].id)
        print(board)
    elif show == "last":
        boards = client.get_boards()
        board = client.get_board(id=boards[-1].id)
        print(board)
    else:
        board = client.get_board(id=show)
        print(board)


show_list_help = """ \n
TEXT=all show all list in a board.\n
TEXT=first show first in a board.\n
TEXT=last show last in a board.\n
"""

board_id_help = """ \n
the board id you want to show its list.
"""


show_list_ex_help = underline("ectrello") + " " + underline("list") + " -boardid" + \
    " 5f2d9bdc " + "--show all"


@cli.command('list')
@click.option("--boardid", required=True, help=board_id_help)
@click.option("--show", required=False, help=show_list_help)
@click.option("--add", required=False, help=show_list_help)
@docstring_parameter(show_list_ex_help)
def list(show, add, boardid):
    """
    Show lists of your trello board\n
    ex: {0}
    """
    if show == "all":
        lists = client.get_lists_in_board(boardid)
        print(lists)
    elif show == "first":
        first_list = client.get_lists_in_board(boardid)[0]
        print(first_list)
    elif show == "last":
        first_list = client.get_lists_in_board(boardid)[-1]
        print(first_list)
    elif (show is None) and (add is None):
        print("Warning: Please select an option --show or --add")
        return
    # elif show is not None:
    #     list = client.get_list(id=show, board_id=boardid)
    #     print(list)
    elif add is not None:
        list = client.post_list(name=add, board_id=boardid)
        board_name = client.get_board(id=boardid).name
        print(f"{list}\nSuccess: A new list has been created in board '{board_name}'")
    else:
        list = client.get_list(id=show)
        print(list)


# new_list = client.post_list(name="Hello10 From Python", board_id=board_id)
if __name__ == '__main__':
    print(board_id_help)
    cli()
