# ECTRELLO
Epilot.Cloud trello cli  -**ectrello**-  is a user-friendly cli which makes interacting with Trello so fun and easy. It has three main functionality:
1- Add a Trello card to a column : `$ ectrello list --boardid <board_id> --add <list_name>`
2- Add a Trello card to a column: `$ ectrello card --listid <board_id> --card <card_name>`
3- Add label and comment on a card (X column of board Y):

## Usage
` ectrello <command> [options]`


These are ectroll commands used in various situations: **board**, **list**, **card**, **label**



### BOARD
`ectrello board [OPTIONS]`
 Display the board of your trello
 >options
`--show all`  display all board of your trello.
`--show first` display first list of your trello.
`--show last`  display last list of your trello.
`--help` display help of the command.

Examplea:
 ```
 $ ectrello board --show all
 $ ectrello board --help
 ```

### LIST

` ectrello list [OPTIONS]`
- Add a Trello card to a column
- Show a Trello card from one of boards

>options
> `--boardid <board_id>` 	the board id to show its list  [**required**].
>`--add <list_name>` 	create new list with name <list_name> in one of your boards.
>`--show <list_id>` 		display the list which its is <list_id>.
>`--show all` 					display all lists in one of your board.
>`--show first`  			display first list in one of your board.
>`--show last`			    display last list in one of your board.
>`--help` display help of the command.

Examples:

 ```
$ ectrello list --boardid <board_id> --add <list_name>
$ ectrello list --boardid <board_id> --show <list_id>
$ ectrello list --boardid <board_id> --show all
$ ectrello list --boardid <board_id> --show first
$ ectrello list --help
 ```



### CARD

` ectrello card [OPTIONS]`
- Add a card to a column
- Display the cards of a list

>options
> `--listid <list_id>`the list id to show its card  [**required**].
>`--add <card_id>` 	add a new card with name.
>`--show <card_id>` 	show one card of an id.
>`--help` display help of the command.

Examples:

 ```
$ ectrello card --listid <list_id> --add <card_name>
$ ectrello card --listid <list_id> --show <card_id>
$ ectrello card --help
 ```
