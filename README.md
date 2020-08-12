# ECTRELLO

## Introduction
(**ectrello** ) is a user-friendly cli which interacts with Trello easily and productively, below are some examples of its functionality:
1. Add a list to a board
2. Add a  card to a column
3. Add a  label on a card
4. Add a  label on a board
5. Add a comment on a card

Examples:
```
$ ectrello list --add <text> --boardid <board_id>
$ ectrello card --add <text> --listid <board_id>
$ ectrello label --add <text> --cardid <card_id>
$ ectrello comment --add <text> --cardid <card_id>
```


## Setup
The cli could be installed in three different ways

1. ###  Python pip

The cli project is hosted on [python package index](https://test.pypi.org/project/ectrello/):
`$ pip install -i https://test.pypi.org/simple/ ectrello`


2. ### Docker

As a requisite a docker must be installed, you may check if it is existed:
`$ docker --version`

The docker will create a persisted image of ectrello cli and will be tagged with a name **ectrello**:
```
$ git clone https://github.com/hadi-alnehlawi/ECTRELLO
$ cd ECTRELLO
$ docker build --tag ectrello .
```

You can interact with **ectrello** by running the container. It is automatically purged after closing
`$ docker run --rm -ti ectrello bash`

You are now able to launch ectrelle on the running docker
`$ ectrello --help`

3. ### Manually
As a perquisite virtualenv package might be installed
`$ virtualenv --version`

If not, please visit this [pypi](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) tutorial for more clarification. Follow the below commands in a sequence
```
$ git clone https://github.com/hadi-alnehlawi/ECTRELLO
$ cd ECTRELLO
$ virtualenv venv
$ source venv/bin/activate
$ pip install .
```
 It is now installed successfully
`$ ectrell --help`

## Usage
` ectrello <command> [options]`

The trello has a couple of  **board**, **list**, **card**, **label**, **comment**   which are controlled by ectrello cli using the below commands:

#### configure
In order to start using the cli, the user must enter its trello API's *token* & *key* by running configure command. As a perquisite the keys  could be generated  form [Trello API](https://trello.com/app-key)

`$ ectrello configure`

####  board
`ectrello board [OPTIONS]`
 Display the board of your trello

 Examples:
 ```
 $ ectrello board --show all
 $ ectrello board --help
 ```
 >options
`--show all`  display all boards of your trello
`--show first` display first list of your trello
`--show last`  display last list of your trello
`--help` display help of the command




####  list

` ectrello list [OPTIONS]`
- Add a card to a column
- Show a card from one of boards

Examples:

 ```
$ ectrello list --boardid <board_id> --add <list_name>
$ ectrello list --boardid <board_id> --show <list_id>
$ ectrello list --boardid <board_id> --show all
$ ectrello list --boardid <board_id> --show first
$ ectrello list --help
 ```

>options
> `--boardid <board_id>` 	the board id to interact with its list  [**required**]
>`--add <list_name>` 	create a new list with a name <list_name> in one of  boards.
>`--show <list_id>` 		display the list of id <list_id>
>`--show all` 					display all lists in a board
>`--show first`  			display first list in a board
>`--show last`			    display last list in a board
>`--help` display help of the command

#### card

` ectrello card [OPTIONS]`
- Add a card to a column
- Display the cards of a list


Examples:

 ```
$ ectrello card --listid <list_id> -add <card_name>  
$ ectrello card --listid <list_id> --show <card_id>  
$ ectrello card --help
 ```
>options
> `--listid <list_id>`the list id to show its card  [**required**]
>`--add <card_id>` 	add a new card with name
>`--show <card_id>` 	show one card of an id
>`--help` display help of the command

#### label

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
> `--add <label_text>` the label text to add [**required**]
>`--cardid <card_id>` 	the card id to add label on
>`--boardid <boardid>` the board id to add label on
>`--help` display help of the command

A  prompt appears asking the user to input a color number, valid values: `yellow`, `purple`, `blue`, `red`, `green`, `orange`, `black`, `sky`, `pink`, `lime`




### comment

` ectrello comment [OPTIONS]`
Add a comment to a column

Examples:

 ```
$ ectrello label --cardid <card_id> --add <text>
$ ectrello label --cardid <card_id> --show all
$ ectrello label --help
 ```

>options
> `--card <card_id>` the card id to show its comments [**required**]
>`--add <text>` 	the comment to add on a card
>`--help` display help of the command

## Testing
In order to run the test you must configure your terminal to interact with Trello API using  your personal *key* and *token*.

`$ ectrell configure`

Once adding your keys, run the test:
```
$ cd TRELLO-CLI
$ python -m unittest -v
```

## Notes
- The cli return json-string values to the terminal for better interactivity and integration.
- If the trello API's key profile was deleted or was wrong, a warning message would appear to notify the user to run the command: ` $ ectrello configure`

- Upon testing random trello objects with random names are created. All objects will be automatically deleted after running the test.
- The test process duration could consume approximately one minutes to complete due to the speed of internet connection and the response from Trello API.
