# ECTRELLO
Epilot.Cloud trello cli  -**ectrello**-  is a user-friendly cli which makes interacting with Trello so fun and easy. It has three main functionality:
1- add a Trello card to a column.
2- add a Trello card to a column.
3- add label and comment on a card (X column of board Y).

## Usage
` ectrello <command> [options]`


These are ectroll commands used in various situations: **board**, **list**, **card**, **label**



### board
`ectrello board [option]`
 Display the board of your trello.
 >options
`--show all`  display all board of your trello
`--show first` display first list of your trello
`--show last`  display last list of your trello

Example:
 `$ ectrello board show --first`

### list
` ectrello list --boardid <boardid> [<options>]`
show and create the list in one of your boards.
>options
>`--add <list_name>` 	create new list with name <list_name> in one of your boards
>`--show <list_id>` 		display the list which its is <list_id>
>`--show all` 					display all lists in one of your board
>`--show first`  			display first list in one of your board
>`--show last`			    display last list in one of your board


Examples:
 `$ ectrello  list -boardid 5f2d9bdc --add "meeting with the team`
 `$ ectrello  list -boardid 5f2d9bdc --show all`
 `$ ectrello  list -boardid 5f2d9bdc --show all`
