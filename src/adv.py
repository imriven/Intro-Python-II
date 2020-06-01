from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                    ["candlestick", "knife"] ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. """,
["chair"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. """,
["rock", "spear"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north.The smell of gold permeates the air. """,
["gold", "herbs"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.The only exit is to the south. """,
["torch", "whip"]),
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
p = Player("Roger", room["outside"])
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
while True:
    print(f"Room: {p.current_room.name}")
    print(f"Description: {p.current_room.description}")
    print("Items: ", end="")
    for i in p.current_room.items:
        print(i, end=" ")
    print()
    print()
    user_input = input("Where do you want to go? ").lower()
    print()
    if user_input == "q":
        break
    elif user_input == "n":
        p.current_room = p.current_room.n_to
    elif user_input == "s":
        p.current_room = p.current_room.s_to
    elif user_input == "e":
        p.current_room = p.current_room.e_to
    elif user_input == "w":
        p.current_room = p.current_room.w_to
    else:
        print("That movement is impossible!!!")

print("Game Over :(")
