from adv import ItemPrinter

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(ItemPrinter):
    def __init__(self, name, race, experiencebar, level, equipment, inventory)
    self.name = name
    self.race = race
    self.experiencebar = experiencebar
    self.level = level
    self.equipment = []
    self.inventory = []

    # def equip(self, inventory, index):

    def pick_up(self, item):
        self.inventory.append(item)

    def equip(self, item):
        if item in self.inventory:
            self.equipment.append(
                self.inventory.pop(self.inventory.index(item)))
        print

    def gainexp(self, exp):
        self.experiencebar += exp
        if self.experiencebar > 10:
            self.experiencebar = self.experiencebar-10
            self.level += 1

    def __str__(self):
        return f'My name is {self.name}'
