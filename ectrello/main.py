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


# class Ectrello(click.Group):
    # def format_help(self, ctx, formatter):
    #     help_txt = "Usage: ectrello <command> [<arg>]\n"
    #     formatter.write(f"{help_txt}")


@click.group()
def cli():
    pass


# ********************************************************************************
# BOARD
show_help_board = """
TEXT=all show all boards. |
TEXT=first show first board. |
TEXT=last show last board. |
"""

board_ex_help = underline("ectrello") + " " + underline("board") + " " + "--show"


@cli.command('board')
@click.option("--show", required=False, help=show_help_board)
@docstring_parameter(board_ex_help)
def board(show):
    """
    Display the board of your Trello\n
    {0}
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


# ********************************************************************************
# LIST

board_id_help = """
TEXT=<board_id> the board id to show its list.
"""
add_list_help = " TEXT=<list_name> add a new list with name."

show_list_help = """
TEXT=<list_id> show one list of id. |
TEXT=all show all list in a board. |
TEXT=first show first in a board. |
TEXT=last show last in a board. |
"""

list_ex_help = underline("ectrello") + " " + underline("list") + " " + "--boardid"\
    + " <board_id> " + "--add " + "<list_name>" + "\n"\
    + underline("ectrello") + " " + underline("list") + " " + "--boardid"\
    + " <board_id> " + "--show <list_id>" + "\n"\
    + underline("ectrello") + " " + underline("list") + " " + "--boardid"\
    + " <board_id> " + "--show all" + "\n"\
    + underline("ectrello") + " " + underline("list") + " " + "--boardid"\
    " <board_id> " + "--show first" + "\n"\
    + underline("ectrello") + " " + underline("list") + " " + "--boardid"\
    " <board_id> " + "--show last" + "\n"\
    + underline("ectrello") + " " + underline("list") + " " + "--help"


@cli.command('list')
@click.option("--boardid", required=True, help=board_id_help)
@click.option("--add", required=False, help=add_list_help)
@click.option("--show", required=False, help=show_list_help)
@docstring_parameter(list_ex_help)
def list(show, add, boardid):
    """
    Add a list to a boad, display the lists of a board \n
    {0}
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
    elif add is not None:
        list = client.post_list(name=add, board_id=boardid)
        print(list)
    else:
        # show is not None
        list = client.get_list(id=show)
        print(list)


# ********************************************************************************
# CARD
list_id_help = """
TEXT=<card_id> the list id to show its card.
"""
add_card_help = " TEXT=<card_name> add a new card with name."

show_card_help = """
TEXT=<card_id> show one card of id. |
TEXT=all show all cards in a list.
"""

card_ex_help = underline("ectrello") + " " + underline("card") + " " + "--listid"\
    + " " + "<list_id> " + "--add" + " " + "<card_name>" + "\n"\
    + underline("ectrello") + " " + underline("card") + " " + "--listid"\
    + " " + "<list_id> " + "--show" + " " + "<card_id>" + "\n"\
    + underline("ectrello") + " " + underline("card") + " " + "--help"


@ cli.command('card')
@click.option("--listid", required=True, help=list_id_help)
@click.option("--add", required=False, help=add_card_help)
@click.option("--show", required=False, help=show_card_help)
@docstring_parameter(card_ex_help)
def card(show, add, listid):
    """
    Add a card to a column, display the cards of a list \n
    {0}
    """
    if show == "all":
        cards = client.get_cards_in_list(listid)
        print(cards)
    elif (show is None) and (add is None):
        print("Warning: Please select an option --show or --add")
        return
    elif add is not None:
        card = client.post_card(name=add, list_id=listid)
        print(card)
    else:
        # show is not None
        card = client.get_card(id=show)
        print(card)


if __name__ == '__main__':
    print(board_id_help)
    cli()
