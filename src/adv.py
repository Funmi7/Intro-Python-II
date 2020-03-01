from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Sword", "This is a sword")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Torch", "Torch gives you light")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Bullets", "Shoot your enemies")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("wand", "Perform some magic")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("treasure", "You did it!!!")]),
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

player = Player(input('Enter name: '), room['outside'])


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

direction = ""
while direction != 'q':
    direction = input(
        f"\nHello {player.name}.\nYou are currently in {player.room}. \nPlease Enter n,s,e,w to continue: ")
    try:
        if direction == "n":
            if player.room.n_to == None:
                print("Try again")
            else:
                player.room = player.room.n_to
        elif direction == 's':
            if player.room.s_to == None:
                print("Try again")
            else:
                player.room = player.room.s_to
        elif direction == 'e':
            if player.room.e_to == None:
                print("Try again")
            else:
                player.room = player.room.e_to
        elif direction == 'w':
            if player.room.w_to == None:
                print("Try again")
            else:
                player.room = player.room.w_to
    except ValueError:
        print('Please your choice is invalid')

    decision = input(f"Please input either to get or drop an item")
    action = decision.split(" ")

    if action[0] == "take":
        item = player.room.get_item(action[1])
        if item == None:
            print("This item is not in the room")
        else:
            player.room.items.remove(item)
            player.add_item(action[1])
            item.on_take()
    elif action[0] == "drop":
        item = player.get_item(action[1])
        if item == None:
            print("Player doesn't have this item")
        else:
            player.room.items.add_item(action[1])
            player.items.remove(item)
            item.on_drop()
