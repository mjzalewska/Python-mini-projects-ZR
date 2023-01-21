class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.impact = kwargs['impact']
        self.user = kwargs['user class']

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
