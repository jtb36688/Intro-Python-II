class NameInventory:
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory

class Description(NameInventory):
    def __init__(self, name, description, inventory=[]):
        super().__init__(name, inventory=inventory)
        self.description = description
        self.itemstrings = [f'\n{item[0]} lays upon the ground' for item in self.inventory]
        #string representation of our class in the console
        #without it: <room.Room object at 0x10c08f4ae> every time
    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}{"".join(self.itemstrings)}'
        