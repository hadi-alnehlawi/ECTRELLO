# ECTRELLO
Epilot.Cloud Trello cli - **ectrello** -  is a user-friendly cli which makes interacting with Trello so fun and easy, below are some examples of its funcaitonality:
1. Add a list to a board: `$ ectrello list --boardid <board_id> --add <list_name>`
2. Add a  card to a column: `$ ectrello card --listid <board_id> --card <card_name>`
3. Add a  label on a card: `$ ectrello label --add <label_text> --cardid <card_id>`
4. Add a  label on a board: `$ ectrello label --add <label_text> --boardid <board_id>`
5. Add a comment on a card: `$ ectrello comment --cardid <card_id> --add <text>`


## Usage
` ectrello <command> [options]`

The trello objects  **board**, **list**, **card**, **label**, **comment**   are controlled by ectrello cli as follow:

### CONFIGURE
In order to start using the cli, the user must enter its trello API's *token* & *key* by running configure command. As a perquisite the keys  could be generated  form [Trello API](https://trello.com/app-key):

`$ ectrello configure`

### BOARD
`ectrello board [OPTIONS]`
 Display the board of your trello
 >options
`--show all`  display all board of your trello.
`--show first` display first list of your trello.
`--show last`  display last list of your trello.
`--help` display help of the command.

Examples:
 ```
 $ ectrello board --show all
 $ ectrello board --help
 ```

### LIST

` ectrello list [OPTIONS]`
- Add a Trello card to a column
- Show a Trello card from one of boards

Examples:

 ```
$ ectrello list --boardid <board_id> --add <list_name>
$ ectrello list --boardid <board_id> --show <list_id>
$ ectrello list --boardid <board_id> --show all
$ ectrello list --boardid <board_id> --show first
$ ectrello list --help
 ```

>options
> `--boardid <board_id>` 	the board id to show its list  [**required**].
>`--add <list_name>` 	create new list with name <list_name> in one of your boards.
>`--show <list_id>` 		display the list which its is <list_id>.
>`--show all` 					display all lists in one of your board.
>`--show first`  			display first list in one of your board.
>`--show last`			    display last list in one of your board.
>`--help` display help of the command.





### CARD

` ectrello card [OPTIONS]`
- Add a card to a column
- Display the cards of a list


Examples:

 ```
$ ectrello card --listid <list_id> --add <card_name>
$ ectrello card --listid <list_id> --show <card_id>
$ ectrello card --help
 ```
>options
> `--listid <list_id>`the list id to show its card  [**required**].
>`--add <card_id>` 	add a new card with name.
>`--show <card_id>` 	show one card of an id.
>`--help` display help of the command.




### LABEL

` ectrello label [OPTIONS]`
- Add a label to a card
- Add a label to a board

Examples:

 ```
$ ectrello label --add <label_text> --cardid <card_id>
$ ectrello label --add <label_text> --boardid <boardid>
$ ectrello label --help
 ```

>options
> `--add <label_text>` the label text to add. [**required**].
>`--cardid <card_id>` 	the card id to add label on.
>`--boardid <boardid>` the board id to add label on.
>`--help` display help of the command.




### COMMENT

` ectrello comment [OPTIONS]`
Add a comment to a column

Examples:

 ```
$ ectrello label --cardid <card_id> --add <comment_text>
$ ectrello label --cardid <card_id> --show all
$ ectrello label --help
 ```

>options
> `--card <card_id>` the card id to show its comments.[**required**].
>`--add <comment_text>` 	the comment to add on a card.
>`--help` display help of the command.



## Notes
- The cli return json string value to terminal for better flexibly and optimization
- If the trello API's key profile was deleted or was worng, a warning message would appear warning the user to run the command: $ ectrello configure
