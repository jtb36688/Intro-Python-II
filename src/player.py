
from lib import NameInventory

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(NameInventory):
    def __init__(self, name, race, equipment, inventory, current_room, level=1, experience_bar=0):
        self.name = name
        self.race = race
        self.experience_bar = experience_bar
        self.level = level
        self.equipment = equipment
        self.inventory = inventory
        self.current_room = current_room

    # def equip(self, inventory, index):

    def add_item(self, item):
        self.inventory.append(item)
        
    def remove_item(self, item):
        self.inventory.remove(item)

    def equip(self, item):
        if item in self.inventory:
            self.equipment.append(
                self.inventory.pop(self.inventory.index(item)))

    def gainexp(self, exp):
        self.experience_bar += exp
        if self.experience_bar > 10:
            self.experience_bar = self.experience_bar-10
            self.level += 1

    def move_player(self, new_room):
        self.current_room = new_room

    def __str__(self):
        return f'My name is {self.name}'

class Dwarf(Player):
    def __init__(self, name, current_room):
        super().__init__(
            name,
            'Dwarf',
            ["Rusty Mace", "Cloth Tunic", "Cloth Pants"],
            ["Bread", "Bread", "Ale", "Ale"],
            current_room
        )

class Elf(Player):
    def __init__(self, name, current_room):
        super().__init__(
            name,
            'Elf',
            ["Rusty Dagger", "Leather Tunic", "Leather Pants"],
            ["Trail Mix", "Trail Mix", "Water", "Water"],
            current_room
        )