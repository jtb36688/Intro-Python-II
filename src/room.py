
from lib import Description

# Implement a class to hold room information. This should have name and
# description attributes.

class Room(Description):
    def __init__(self, name, description, inventory=[]):
        super().__init__(name, description, inventory=inventory)
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def add_item(self, item):
        self.inventory.append(item)