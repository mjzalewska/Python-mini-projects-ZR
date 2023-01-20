class Scene:
    def __init__(self, **kwargs):
        self.no = kwargs['no']
        self.name = kwargs['name']
        self.intro = kwargs['intro']
        self.description = kwargs['description']

        self.items = [item['name'] for item in kwargs['items']]

    def show_intro(self):
        return self.intro

    def __str__(self):
        return self.description

    def enumerate_items(self):
        if len(self.items) > 0:
            for item in self.items:
                return item
        else:
            return "Nothing in here..."

