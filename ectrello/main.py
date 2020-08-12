import click
from pathlib import Path
from os import path
import json
from .trello.client import Client
from .trello.config import Configuration

# from trello.client import Client

path = Path(path.expanduser("~/.ectrello-config"))
configuration = Configuration(config_path=path)


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


# ********************************************************************************
# CONFIGURE


configuraiton_ex_help = "ectrello" + " " + "configuraiton" + 40 * " " + "\n"\
    + "ectrello" + " " + "configuraiton" + " " + "--help" + " " + 40 * " " + "\n"


@ cli.command('configure')
@ docstring_parameter(configuraiton_ex_help)
def configure():
    """
    Configure you board API keys\n
    {0}
    """
    msg1 = "Welcome to ectrello..\n"
    msg2 = "This CLI is developed by @Hadi.Alnehalwi as a code excerice for Epilot.Cloud\n"
    msg3 = "You are going to write your trello API keys to interacte with ectrell cli\n"
    msg4 = "Do you want to coninture'?"
    confirm_text =\
        "\n"\
        + len(msg2) * "*" + "\n"\
        + msg1\
        + msg2\
        + len(msg2) * "*" + "\n\n"\
        + msg3\
        + msg4

    if click.confirm(confirm_text):
        configuration.get_config()
        if configuration.check_config():
            configuration.overwrite_config()
        else:
            configuration.post_config()
    if configuration.check_with_trello():
        pass
    else:
        print("Trello API's keys are not correct. Please try again.!")


# ********************************************************************************
# BOARD
show_help_board = """
TEXT=all show all boards. |
TEXT=first show first board. |
TEXT=last show last board. |
"""

board_ex_help = "ectrello" + " " + "board" + " " + "--show"\
    + " " + "<option>" + 40 * " " + "\n" + "ectrello" + " " + "board" + " " + "--help"


@ cli.command('board')
@ click.option("--show", required=False, help=show_help_board)
@ docstring_parameter(board_ex_help)
def board(show):
    """
    Display the board of your Trello\n
    {0}
    """

    if configuration.check_with_trello():
        client = Client(configuration.key, configuration.token)
        if show == "all" or show is None:
            boards = client.get_boards()
            print(boards)
        elif show == "first":
            boards = client.get_boards()
            if len(boards) > 0:
                board = client.get_board(id=boards[0].id)
            else:
                board = []
            print(board)
        elif show == "last":
            boards = client.get_boards()
            if len(boards) > 0:
                board = client.get_board(id=boards[-1].id)
            else:
                board = []
            print(board)
        else:
            board = client.get_board(id=show)
            print(board)
    else:
        print({"status code": 400,
               "message": "Trello API's keys are not correct. Run this commnad first $ectroll configure"})


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

list_ex_help = ""\
    + "ectrello list --add <list_name> --boardid <board_id>" + 40*" " + "\n"\
    + "ectrello list --show <list_id> --boardid <board_id>" + 40*" " + "\n"\
    + "ectrello list --show all --boardid <board_id>" + 40*" " + "\n"\
    + "ectrello list --show first --boardid <board_id>" + " " + + 40*" " + "\n"\
    + "ectrello list --show last --boardid <board_id>" + " " + + 40*" " + "\n"\
    + "ectrello list --help"


@ cli.command('list')
@ click.option("--add", required=False, help=add_list_help)
@ click.option("--boardid", required=True, help=board_id_help)
@ click.option("--show", required=False, help=show_list_help)
@ docstring_parameter(list_ex_help)
def list(show, add, boardid):
    """
    Add a list to a boad, display the lists of a board \n
    {0}
    """
    if configuration.check_with_trello():
        client = Client(configuration.key, configuration.token)
        if (show == "all") and (boardid is not None):
            lists = client.get_lists_in_board(boardid)
            print(lists)
        elif (show == "first") and (boardid is not None):
            if len(client.get_lists_in_board(boardid)) > 0:
                first_list = client.get_lists_in_board(boardid)[0]
            else:
                first_list = []
            print(first_list)
        elif (show == "last") and (boardid is not None):
            if len(client.get_lists_in_board(boardid)) > 0:
                first_list = client.get_lists_in_board(boardid)[-1]
            else:
                first_list = []
            print(first_list)
        elif (show is None) and (add is None):
            print({"status code": 404, "message": "Please select an option --show or --add"})
            return
        elif (add is not None) and (boardid is not None):
            list = client.post_list(name=add, board_id=boardid)
            print(list)
        else:
            # show is not None
            list = client.get_list(id=show)
            print(list)

    else:
        print({"status code": 400,
               "message": "Trello API's keys are not correct. Run this commnad first $ectroll configure"})


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
    if configuration.check_with_trello():
        client = Client(configuration.key, configuration.token)
        if (show == "all") and (listid is not None):
            cards = client.get_cards_in_list(listid)
            print(cards)
        elif (show is None) and (add is None):
            print({"status code": 404, "message": "Please select an option --show or --add"})
            return
        elif (add is not None) and (listid is not None):
            card = client.post_card(name=add, list_id=listid)
            print(card)
        else:
            # show is not None
            card = client.get_card(id=show)
            print(card)
    else:
        print({"status code": 400,
               "message": "Trello API's keys are not correct. Run this commnad first $ectroll configure"})


# ********************************************************************************
# LABEL

label_add_help = """
TEXT=<label_text> the label text to add.
"""
card_id_help = """
TEXT=<card_id> the card id to add label on.
"""

board_id_help = """
TEXT=<board_id> the board id to add label on.
"""
add_label_help = " TEXT=<label_text> add a new label with text."


label_ex_help = "ectrello" + " " + "label" + " " + "--add" + " " + "<label_text>"\
    + " " + "--cardid" + " " + "<card_id>" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "label" + " " + "--add"\
    + " " + "<label_text> " + "--boardid" + " " + "<boardid>" + 40*" " + "\n"\
    + " " + "ectrello" + " " + "label" + " " + "--help"


@ cli.command('label')
@ click.option("--add", required=True, help=label_add_help)
@ click.option("--cardid", required=False, help=card_id_help)
@ click.option("--boardid", required=False, help=board_id_help)
@ docstring_parameter(label_ex_help)
def label(add, cardid, boardid):
    """
    Add a label to a column, display the labels of a board \n
    {0}
    """
    if configuration.check_with_trello():
        client = Client(configuration.key, configuration.token)
        if (cardid is not None):
            label = client.get_label(id=add)
            if type(label) is tuple:
                # label is not existed so create a new one on board of card
                card = client.get_card(cardid)
                board_id = card.board_id
                label = client.post_label_to_baord(name=add, board_id=board_id)
                label_id = label.id
                card_id = card.id
                new_label = client.post_label_to_card(id=label_id, card_id=card_id)
                print(new_label)
            else:
                # existing label
                label_id = label.id
                new_label = client.post_label_to_card(id=label_id, card_id=cardid)
                print(new_label)

        elif (cardid is None) and (boardid is not None):
            label = client.post_label_to_baord(name=add, board_id=boardid)
            print(label)
        elif (cardid is None) and (boardid is None):
            print({"status code": 404, "message": "Please select an option --cardid or --boardid"})
            return
        else:
            return
    else:
        print({"status code": 400,
               "message": "Trello API's keys are not correct. Run this commnad first $ectroll configure"})


# ********************************************************************************
# COMMENT
card_id_help = """
TEXT=<card_id> the card id to show its comments.
"""
add_comment_help = " TEXT=<comment_text> add a new comment  on a card."

show_comment_help = """
TEXT=<card_id> show comments of card id
"""

comment_ex_help = "ectrello" + " " + "comment" + " " + "--cardid"\
    + " " + "<card_id>" + " " + "--add" + " " + "<comment_text>" + 40 * " " + "\n"\
    + "ectrello" + " " + "comment" + " " + "--cardid"\
    + " " + "<card_id>" + " " + "--show" + " " + "all" + 40 * " " + "\n"\
    + "ectrello" + " " + "card" + " " + "--help"


@ cli.command('comment')
@ click.option("--cardid", required=True, help=card_id_help)
@ click.option("--add", required=False, help=add_comment_help)
@ click.option("--show", required=False, help=add_comment_help)
@ docstring_parameter(comment_ex_help)
def comment(show, add, cardid):
    """
    Add a comment to a column\n
    {0}
    """
    if configuration.check_with_trello():
        client = Client(configuration.key, configuration.token)
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

    else:
        print({"status code": 400,
               "message": "Trello API's keys are not correct. Run this commnad first $ectroll configure"})


if __name__ == '__main__':
    print(board_id_help)
    cli()
