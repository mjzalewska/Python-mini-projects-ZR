class Item:
    def __init__(self, **kwargs):
        for i in range(len(kwargs['items'])):
            self.name = kwargs['items'][i]['name']
            self.description = kwargs['items'][i]['description']
            self.impact = kwargs['items'][i]['impact']

    def __str__(self):
        print(self.description)

    def show_item_stats(self):
        print(f"-{self.name} stats-")
        for k, v in self.impact.items():
            print(f"{k}:{v}")

    def boost_char_stats(self, character):
        for key, value in self.impact.items():
            character.stats[key] = character.stats[key] + self.impact[key]
        return character.stats

    @staticmethod
    def take_item(scene, hero):
        if scene.items:
            print('You can only choose one item. Choose wisely!')
            while True:
                chosen_item = input('Which item would you like to take?').title()
                if chosen_item not in scene.items():
                    print('Sorry, no such item here!')
                else:
                    hero.add_item(chosen_item)
                    break

    @staticmethod
    def use_item(hero):
        print("Your inventory:")
        hero.show_inventory()
        print("Which item would you like to use?")
        while True:
            item_choice = input().title()
            if item_choice not in hero.inventory():
                print('Sorry there\'s nothing like that in your backpack!')
            else:
                return item_choice

# from character import Hero
#
# values = {
#     "class": "Elf",
#     "stats":
#         {"level": 10,
#          "hp": 10,
#          "mp": 8,
#          "attack": 8,
#          "defense": 8
#          },
#     "weapon type": "Bow",
#     "max inventory": 6,
#     "description": "Skilled in swordsmanship and archery. Can use faerie magic and prepare potions",
#     "inventory": ["Silver Bow"]
# }
#
# item_values = {"items":[
#   {
#     "name": "Buster Sword",
#     "description": "A long steel broadsword, very powerful in close-range combat",
#     "impact": {
#       "hp": 0,
#       "mp": 0,
#       "attack": 7,
#       "defense": 3
#     }
#   },
#   {
#     "name": "Silver Bow",
#     "description": "A silver emerald-encrusted bow",
#     "impact": {
#       "hp": 0,
#       "mp": 2,
#       "attack": 4,
#       "defense": 0
#     }
#   }
#     ]
# }
#
# elf_char = Hero(**values)
# print(elf_char.stats)
# item_1 = Item(**item_values)
# item_1.show_item_stats()
# elf_char.add_item('Health Potion')
# elf_char.show_inventory()
# item_1.boost_char_stats(elf_char)
# print(elf_char.stats)