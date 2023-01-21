# implement use_item method

class Character:

    def __init__(self, **kwargs):
        self.stats = kwargs['stats']
        self.description = kwargs['description']
        self.inventory = kwargs['inventory']
        self.max_inventory = kwargs['max_inventory']

    def __str__(self):
        return self.description

    def add_item(self, item):
        if len(self.inventory) < self.max_inventory:
            self.inventory.append(item)
        else:
            print("You cannot carry any more items!")

    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            print("Your backpack is empty!")

    def show_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                return item
        else:
            return "There's nothing in your backpack"

    def use_item(self, item):
        pass