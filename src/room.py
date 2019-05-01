from adv import ItemPrinter

# Implement a class to hold room information. This should have name and
# description attributes.

class Room(ItemPrinter):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []

    def add_item(self, item):
    self.inventory.append(item)