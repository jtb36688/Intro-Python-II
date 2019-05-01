from room import Room

# Declare all the rooms


room = {
    'orcHill': Room("Outside Orc Encampment",
                    """Before you there are several orc camps, threatening to raid the elf city. 
    To the south, is the elf city Kelethin"""),

    'kelethinOL': Room("Orc Lift",
                       """North of you, the orc encampment beckons.
                      To the west, is the closest lift to enter the treetop elf city Kelethin. 
                      To the south, are the other lifts to reach the city."""),

    'kelethinPL': Room("Discord Lift",
                       """North of you is the northern lift to reach the city.
                      To the west, is the closest lift to enter the treetop elf city Kelethin. 
                      To the south, is the southern lift to reach the city."""),

    'kelethinNL': Room("Grand Overlook",
                       """To the north, are the other lifts to reach the city.
    To the west, is the closest lift to enter the treetop elf city Kelethin.
    To the south, is the path through the forest of Greater Faydark."""),

    'gfayPath': Room("Dark Forested Path",
                     """The bending path follows through the forest of Greater Faydark.
    To the north is the elf city of Kelethin.
    To the west the path leads into the Butcherblock mountain range."""),

    'bbpath': Room("Butcherblock Mountains Path",
                   """The path winds through the expansive Butcherblock Mountains.
    To the west, the path continues onward into the mountains.
    To the east, the path leads into the mouth of the Greater Faydark forest."""),

    'crossroads': Room("Butcherblock Mountains Crossroads",
                    """The path has lead to a three-split crossroad, where there is a nearby dwarf encampment.
    To the north, the path continues to the dwarf city of Kaladim.
    To the south, the path leads to an dark and spooky mansion.
    to the east, the path leads onward towards a forest."""),

    'unrest': Room("Estate of Unrest",
                   """The path has ended at a spooky mansion. 
    There are skeletons and zombies suddenly surrounding you from every direction.
    You shouldn't have come here!"""
                   ),

    'kaladim': Room("Dwarf City of Kaladim",
                    """You have entered the dwarf city of Kaladim, which is dug deep into the mountainside.
    The place looks fancy for being inside a mine, with marble buildings and forges where smiths are working.
    To the north, the path leads past several shops into the Kaladim Warrior's guild.
    To the south, the path leads out into the Butcherblock Mountain Range."""),

    "warriorguild": Room("Dwarf Warrior Guild",
    """You have entered the dwarven warrior guild. 
    The guildmaster Canloe Nusback nods at you from the a table at the back of the guild.
    The exit back to Kaladim is to the south."""
    )
}


# Link rooms together

room['orcHill'].s_to = room['kelethinOL']
room['kelethinOL'].s_to = room['keletinPL']
room['kelethinOL'].n_to = room['orcHill']
room['kelethinPL'].s_to = room['keletinNL']
room['kelethinPL'].n_to = room['kelethinOL']
room['kelethinNL'].s_to = room['gfayPath']
room['kelethinNL'].n_to = room['kelethinPL']
room['gfayPath'].n_to = room['keletinNL']
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
#

# Make a new player object that is currently in the 'outside' room.

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

Thorin = Player("Thorin", "Dwarf", 0, 1, [
                "Rusty Mace", "Cloth Tunic", "Cloth Pants"], ["Bread", "Bread", "Water", "Water"])


class ItemPrinter:
    def __init__(self):
        pass

    def print_contents(self):
        for i in self.inventory:
            print(i)
