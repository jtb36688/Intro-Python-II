from room import Room
from player import Dwarf
from player import Elf
from item import Item

room = {
    'orcHill': Room("Outside Orc Encampment",
                    """Before you there are several orc camps, threatening to raid the elf city.\nTo the south, is the elf city Kelethin""",
                    ['Orc Belt']),

    'kelethinOL': Room("Orc Lift",
                       """North of you, the orc encampment beckons.\nTo the west, is the closest lift to enter the treetop elf city Kelethin.\nTo the south, are the other lifts to reach the city."""),

    'kelethinPL': Room("Discord Lift",
                       """North of you is the northern lift to reach the city.\nTo the west, is the closest lift to enter the treetop elf city Kelethin.\nTo the south, is the southern lift to reach the city."""),

    'kelethinNL': Room("Newbie Lift",
                       """To the north, are the other lifts to reach the city.\nTo the west, is the closest lift to enter the treetop elf city Kelethin.\nTo the south, is the path through the forest of Greater Faydark."""),

    'gfayPath': Room("Dark Forested Path",
                     """The bending path follows through the forest of Greater Faydark.\nTo the north is the elf city of Kelethin.\nTo the west the path leads into the Butcherblock mountain range.""",
                     ['Magic Wand']),

    'bbpath': Room("Butcherblock Mountains Path",
                   """The path winds through the expansive Butcherblock Mountains.\nTo the west, the path continues onward into the mountains.\nTo the east, the path leads into the mouth of the Greater Faydark forest."""),

    'crossroads': Room("Butcherblock Mountains Crossroads",
                       """The path has lead to a three-split crossroad, where there is a nearby dwarf encampment.\nTo the north, the path continues to the dwarf city of Kaladim.\nTo the south, the path leads to an dark and spooky mansion.\nTo the east, the path leads onward towards a forest.""",
                       ['Blood-covered Note']),

    'unrest': Room("Estate of Unrest",
                   """The path has ended at a spooky mansion.\nThere are skeletons and zombies suddenly surrounding you from every direction.\nYou shouldn't have come here!"""
                   ),

    'kaladim': Room("Dwarf City of Kaladim",
                    """You have entered the dwarf city of Kaladim, which is dug deep into the mountainside.\nThe place looks fancy for being inside a mine, with marble buildings and forges where smiths are working.\nTo the north, the path leads past several shops into the Kaladim Warrior's guild.\nTo the south, the path leads out into the Butcherblock Mountain Range.""",
                    ['Dusty Note']),

    "warriorguild": Room("Dwarf Warrior Guild",
                         """You have entered the dwarven warrior guild.\nThe guildmaster Canloe Nusback nods at you from the a table at the back of the guild.\nThe exit back to Kaladim is to the south."""
                         )
}

item = {
    "dustynote": Item("Dusty Note", "It reads: You can gain experience by turning orc belts in at Kaladim Warrior Guild."),
    "bloodnote": Item('Blood-covered Note', 'It reads: Dont go to the mansion!'),
    'magicwand': Item('Magic Wand', 'It glows faintly with some remaining power'),
    "orcbelt": Item("Orc Belt", "Terribly-smelling belt from a fallen orc")
}

# 'Blood-covered Note'= item["bloodnote"]
# 'Magic Wand'= item["magicwand"]
# "Orc Belt" = item["orcbelt"]



start_location = {
    'dwarf': room['kaladim'],
    'elf': room['kelethinNL'],
}


def raceOrigins(name, type):
    if type == 'dwarf':
        return Dwarf(name, start_location[type])
    elif type == 'elf':
        return Elf(name, start_location[type])


# Link rooms together

room['orcHill'].s_to = room['kelethinOL']
room['kelethinOL'].s_to = room['kelethinPL']
room['kelethinOL'].n_to = room['orcHill']
room['kelethinPL'].s_to = room['kelethinNL']
room['kelethinPL'].n_to = room['kelethinOL']
room['kelethinNL'].s_to = room['gfayPath']
room['kelethinNL'].n_to = room['kelethinPL']
room['gfayPath'].n_to = room['kelethinNL']
room['gfayPath'].w_to = room['bbpath']
room['bbpath'].w_to = room['crossroads']
room['bbpath'].e_to = room['gfayPath']
room['crossroads'].s_to = room['unrest']
room['crossroads'].e_to = room['bbpath']
room['crossroads'].n_to = room['kaladim']
room['kaladim'].s_to = room['crossroads']
room['kaladim'].n_to = room['warriorguild']
room['warriorguild'].s_to = room['kaladim']


#
# Main


# Make a new player object that is currently in the 'outside' room.
# get_room should get the string input and turn that into a class property
# 'n' -> current_room.n_to

def get_room(cmd, current_room):
    if cmd == 'n':
        return current_room.n_to
    elif cmd == 's':
        return current_room.s_to
    elif cmd == 'e':
        return current_room.e_to
    elif cmd == 'w':
        return current_room.w_to


def get_room2(cmd, current_room):
    moving = cmd + '_to'
    return getattr(current_room, moving, None)


def intro():
    print("Welcome to the Everquest Faydwer Text Adventure, by Jacob Bryan")
    print("enter character name to continue..")
    global name
    name = input(" -> ")


def makePlayer():
    print("do you want to be a Dwarf or an Elf?")
    global race
    race = input(" -> ")


directions = ["n", "s", "w", "e"]

while True:
    if 'player' not in globals():
        intro()
        makePlayer()
        if race == "dwarf" or "elf":
            player = raceOrigins(name, race)
    else:
        print(f"You are {player.name}, level {player.level} {player.race}\nInput N/W/S/E to travel, input USE, EQUIP, GET, DROP -itemname- to interact with items, input Q to quit")
        for item in player.inventory:
            print(f'You are holding {item}')
        print(player.current_room)
        if player.current_room.name == "Estate of Unrest":
            unrestcmd = input(
                "The undead are closing in, what do you do? Hint: Type use ITEMNAME to use an item ->")
            # if unrestcmd == "use rusty mace" or unrestcmd == "use rusty dagger"
            #      unrestcmd = input("You fight off one zombie with your weapon and it breaks! What do you do now? ->")
            if unrestcmd == "use magic wand" and "Magic Wand" in player.inventory:
                print(
                    "The wand glows bright!\n All the dead fall down and become, well, dead again.\nYou escape back into the mountains!")
                player.move_player(room['crossroads'])
            else:
                print(
                    "Your foolish attempts to escape are futile. The dead swarm you and you are eaten alive.")
                break
        else:
            cmd = input(" ->")
            if cmd in directions:
                new_room = get_room(cmd, player.current_room)
                if new_room is not None:
                    player.move_player(new_room)
                else:
                    print("You can't move any further in that direction")
            elif cmd.split(' ')[0] == 'equip' or cmd.split(' ')[0] == 'get' or cmd.split(' ')[0] == 'drop':
                if cmd.split(' ')[0] == 'equip':
                    activeItem = cmd[6:]
                    if activeItem in player.inventory:
                        player.equip(activeItem)
                        print(f'You have equipped the {activeItem}!')
                    else:
                        print(f'You do not own the {activeItem}!')
                if cmd.split(' ')[0] == 'get':
                    activeItem = cmd[4:]
                    if activeItem in player.current_room.inventory:
                        player.current_room.remove_item(activeItem)
                        player.add_item(activeItem)
                        print(f'You have picked up the {activeItem}!')
                    else:
                        print(f'You cannot find a {activeItem} nearby.')
                if cmd.split(' ')[0] == 'drop':
                    activeItem = cmd[5:]
                    if activeItem in player.inventory:
                        player.remove_item(activeItem)
                        player.current_room.add_item(activeItem)
                        print(f'You have dropped {activeItem} on the ground!')
                    else:
                        print(f'You do not own the {activeItem}!')
            elif cmd == 'q':
                break
            else:
                print("I don't know what that means!")

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


# class ItemPrinter:
#     def __init__(self):
#         pass

#     def print_contents(self):
#         for i in self.inventory:
#             print(i)
