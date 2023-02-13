class Scene:
    def __init__(self, **kwargs):
        self.no = kwargs['no']
        self.name = kwargs['name']
        self.intro = kwargs['intro']
        self.enemy = kwargs['enemy']
        self.description = kwargs['description']
        self.next_scene = kwargs['next scene']
        self.items = [item['name'] for item in kwargs['items']]

    def show_intro(self):
        for line in self.intro.split('.'):
            print(line)

    def has_enemy(self):
        if self.enemy:
            return True
        return False

    def __str__(self):
        return self.description

    def enumerate_items(self, character):
        if len(self.items) > 0:
            print("There are some interesting items here...")
            for item in self.items:
                item_type = item.lower().split()[1]
                weapons = ['bow', 'sword', 'staff']
                if (item_type == character.weapon.lower()) or \
                        (item_type not in weapons):
                    print(item)
        else:
            print("Nothing interesting here for you...")

    def remove_items(self):
        self.items.clear()


