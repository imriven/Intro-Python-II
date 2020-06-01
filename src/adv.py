from room import Room
from player import Player
from item import Item
from color import Color
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("candlestick"), Item("knife")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. """,
                     [Item("chair")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. """,
                     [Item("rock"), Item("spear")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north.The smell of gold permeates the air. """,
                     [Item("gold"), Item("herbs")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.The only exit is to the south. """,
                     [Item("torch"), Item("whip")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player("You", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


#colors
blue = Color.BLUE
purple = Color.PURPLE
color_end = Color.END
cyan = Color.CYAN
red = Color.RED
green = Color.GREEN

def change_room(direction):
    try:
        if direction == "n":
            p.current_room = p.current_room.n_to
        elif direction == "s":
            p.current_room = p.current_room.s_to
        elif direction == "e":
            p.current_room = p.current_room.e_to
        elif direction == "w":
            p.current_room = p.current_room.w_to
        else:
            print(red + "That movement is impossible!!!" + color_end)
    except AttributeError:
        print(red + "cannot move in that direction from this room" + color_end)


def item_in_room(room, item_name):
    for item in room.items:
        if item.name == item_name:
            return item
    return False

def player_has_item(item_name):
    for item in p.inventory:
        if item.name == item_name:
            return item
    return False


def do_action(action, item):
    if action in ["take", "get"]:
        item_object = item_in_room(p.current_room, item)
        if item_object:
            p.current_room.items.remove(item_object)
            p.inventory.append(item_object)
            item_object.on_take()
        else:
            print(red + "no such item in here" + color_end)
    elif action in ["drop"]:
        item_object = player_has_item(item)
        if item_object:
            p.inventory.remove(item_object)
            p.current_room.items.append(item_object)
            item_object.on_drop()
        else:
            print(red + "you don't have this item in your inventory" + color_end)
    elif action in ["show"]:
        if item == "inventory":
            print(f"{[i.name for i in p.inventory]}")

instructions = "Instructions: You may type in" + purple + " get/take item " + color_end + "to grab an item \nYou can type in" + green + " drop item " + color_end + " to drop an item from your inventory. \nYou may press" + cyan + " n, s, e, or w " + color_end + "to enter a new room"

while True:
    print(f"You Are: {p.current_room.name}")
    print(f"You See: {p.current_room.description}")
    print(f"Items: {' / '.join([i.name for i in p.current_room.items])}")
    print()
    user_input = input(
        "What do you want to do? \n type 'help' for more instructions ").lower().split(" ")
    print()
    if user_input[0] == "q":
        break
    elif user_input[0] == "help":
        print(instructions)
        print()
        continue
    if len(user_input) == 1:
        change_room(*user_input)
    elif len(user_input) == 2:
        do_action(*user_input)
    else:
        print(red + "unknown command" + color_end)


print(blue + "Game Over :(" + color_end)
