class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.impact = kwargs['impact']

    def __str__(self):
        return self.description

    def show_item_stats(self):
        print(f"-{self.name} stats-")
        for k, v in self.impact.items():
            print(f"{k}:{v}")

    def boost_char_stats(self, character):
        for key, value in self.impact.items():
            character.stats[key] = character.stats[key] + self.impact[key]
        return character.stats

    def take_item(self, scene, hero):
        if scene.items:
            print('You can only choose one item. Choose wisely!')
            while True:
                chosen_item = input('Which item would you like to take?').title()
                if chosen_item not in scene.items():
                    print('Sorry, no such item here!')
                else:
                    hero.add_item(chosen_item)
                    break

    def use_item(self, hero):
        print("Your inventory:")
        hero.show_inventory()
        print("Which item would you like to use?")
        while True:
            item_choice = input().title()
            if item_choice not in hero.inventory():
                print('Sorry there\'s nothing like that in your backpack!')
            else:
                return item_choice


