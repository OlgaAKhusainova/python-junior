class Coffee:
    def __init__(self, name):
        self.name = name
        if name == 'capuccino':
            self.ingridients = ['espresso', 'milk']
        elif name == 'latte':
            self.ingridients = ['espresso', 'cream']
        elif name == 'iced':
            self.ingridients = ['espresso', 'ice-cream']
        else: self.ingridients = []
    
    def get_recipe(self):
        print(self.name + ': ' + str(self.ingridients))
        return self
    
cup = Coffee('capuccino')
cup.get_recipe()
