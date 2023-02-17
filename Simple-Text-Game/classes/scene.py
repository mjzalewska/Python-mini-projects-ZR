class Scene:
    def __init__(self, **kwargs):
        self.no = kwargs['no']
        self.name = kwargs['name']
        self.intro = kwargs['intro']
        self.enemy = kwargs['enemy']
        self.description = kwargs['description']
        self.next_scene = kwargs['next scene']
        self.items = [item['name'] for item in kwargs['items']]

    def __str__(self):
        return self.description

    def show_intro(self):
        for line in self.intro.split('.'):
            print(line)

    def has_enemy(self):
        if self.enemy:
            return True
        return False

    def enumerate_items(self):
        if len(self.items) > 0:
            for item in self.items:
                print(item)
        else:
            print("Nothing interesting here for you...")



