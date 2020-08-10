import click
from .trello.client import Client
# from trello.client import Client


key = "0581b1db0a42258051a8a25fb301e247"
token = "e6985b1a4afdfb4168814ca486e76ff704e171d5751ce9db8c96731f8b1cc0cb"
client = Client(key, token)


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

board_ex_help = "ectrello" + " " + "board" + " " + "--show"\
    + " " + "<option>" + 40 * " " + "\n" + "ectrello" + " " + "board" + " " + "--help"


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

list_ex_help = "ectrello" + " " + "list" + " " + "--boardid"\
    + " " + "<board_id>" + "--add " + "<list_name>" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "list" + " " + "--boardid"\
    + " " + "<board_id>" + " " + "--show" + " " + "<list_id>" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "list" + " " + "--boardid"\
    + " " + "<board_id>" + " " + "--show all" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "list" + " " + "--boardid"\
    + " " + "<board_id>" + " " + "--show first" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "list" + " " + "--boardid"\
    + " " + "<board_id>" + " " + "--show last" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "list" + " " + "--help"\



@ cli.command('list')
@ click.option("--add", required=False, help=add_list_help)
@ click.option("--boardid", required=False, help=board_id_help)
@ click.option("--show", required=False, help=show_list_help)
@ docstring_parameter(list_ex_help)
def list(show, add, boardid):
    """
    Add a list to a boad, display the lists of a board \n
    {0}
    """
    if (show == "all") and (boardid is not None):
        lists = client.get_lists_in_board(boardid)
        print(lists)
    elif (show == "first") and (boardid is not None):
        first_list = client.get_lists_in_board(boardid)[0]
        print(first_list)
    elif (show == "last") and (boardid is not None):
        first_list = client.get_lists_in_board(boardid)[-1]
        print(first_list)
    elif (show is None) and (add is None):
        print("Warning: Please select an option --show or --add")
        return
    elif (add is not None) and (boardid is not None):
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

card_ex_help = "ectrello" + " " + "card" + " " + "--listid"\
    + " " + "<list_id> " + "--add" + " " + "<card_name>" + 40*" " + "\n"\
    + "ectrello" + " " + "card" + " " + "--listid"\
    + " " + "<list_id> " + "--show" + " " + "<card_id>" + 40*" " + "\n"\
    + "ectrello" + " " + "card" + " " + "--help"\



@ cli.command('card')
@ click.option("--add", required=False, help=add_card_help)
@ click.option("--listid", required=False, help=list_id_help)
@ click.option("--show", required=False, help=show_card_help)
@ docstring_parameter(card_ex_help)
def card(show, add, listid):
    """
    Add a card to a column, display the cards of a list \n
    {0}
    """
    if (show == "all") and (listid is not None):
        cards = client.get_cards_in_list(listid)
        print(cards)
    elif (show is None) and (add is None):
        print("Warning: Please select an option --show or --add")
        return
    elif (add is not None) and (listid is not None):
        card = client.post_card(name=add, list_id=listid)
        print(card)
    else:
        # show is not None
        card = client.get_card(id=show)
        print(card)


# ********************************************************************************
# LABEL
label_id_help = """
TEXT=<card_id> the list id to show its card.
"""
add_label_help = " TEXT=<card_name> add a new card with name."

show_label_help = """
TEXT=<card_id> show one card of id. |
TEXT=all show all cards in a list.
"""

label_ex_help = "ectrello" + " " + "card" + " " + "--listid"\
    + " " + "<list_id>" + " " + "--add" + " " + "<card_name>" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "card" + " " + "--listid"\
    + " " + "<list_id> " + "--show" + " " + "<card_id>" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "card" + " " + "--help"


@ cli.command('label')
@ click.option("--add", required=False, help=add_card_help)
@ click.option("--listid", required=True, help=list_id_help)
@ click.option("--show", required=False, help=show_card_help)
@ docstring_parameter(label_ex_help)
def label(show, add, listid):
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


# ********************************************************************************
# COMMENT
card_id_help = """
TEXT=<card_id> the card id to show its comment.
"""
add_comment_help = " TEXT=<comment_text> add a new comment on a card."

show_comment_help = """
TEXT=<card_id> show comments of card id
"""

comment_ex_help = "ectrello" + " " + "comment" + " " + "--cardid"\
    + " " + "<card_id>" + " " + "--add" + " " + "<text>" + 100*" " + "\n"\
    + " " + "ectrello" + " " + "card" + " " + "--help"


@ cli.command('comment')
@ click.option("--add", required=False, help=add_comment_help)
@ click.option("--cardid", required=True, help=card_id_help)
@ click.option("--show", required=False, help=add_comment_help)
@ docstring_parameter(comment_ex_help)
def comment(show, add, cardid):
    """
    Add a comment to a column\n
    {0}
    """
    if (show is None) and (add is None):
        print("Warning: Please select an option --show or --add")
        return
    elif (show == "all"):
        comments = client.get_comments_in_card(card_id=cardid)
        print(comments)
    else:
        # add is not None
        comment = client.post_comment_card(text=add, card_id=cardid)
        print(comment)


if __name__ == '__main__':
    print(board_id_help)
    cli()
