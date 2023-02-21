class Item:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.description = kwargs['description']
        self.impact = kwargs['impact']
        self.is_collectible = kwargs['collectible']
        self.complementary_item = kwargs['complementary item']
        self.action_result = kwargs['result']

    def __str__(self):
        print(self.description)

    def show_item_stats(self, name):
        print(f"-{name} stats-")
        for k, v in self.impact.items():
            print(f"{k}:{v}")

    def boost_char_stats(self, character):
        for key, value in self.impact.items():
            character.stats[key] = character.stats[key] + self.impact[key]
        return character.stats

    def reduce_char_stats(self, character):
        for key, value in self.impact.items():
            character.stats[key] = character.stats[key] - self.impact[key]
        return character.stats


