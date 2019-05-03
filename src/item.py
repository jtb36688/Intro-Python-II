from lib import Description

class Item(Description):
    def __init__(self, name, description, inventory=[]):
        super().__init__(name, description, inventory=inventory)