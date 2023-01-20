class Enemy:

    def __init__(self, **kwargs):
        self.stats = kwargs['stats']
        self.description = kwargs['description']
        self.enemy_class = kwargs['class']

    def __str__(self):
        return self.description

    def show_stats(self):
        return f"level:{self.stats['level']}\nHP:{self.stats['hp']}\nMP:{self.stats['mp']}\n" \
               f"ATTACK:{self.stats['attack']}\nDEFENCE{self.stats['defence']}"