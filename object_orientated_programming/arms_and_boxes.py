import random

class Arm:
    def __init__(self, name, mean, std):
        '''Builds an Arm for a Fighter
        Params:
        - mame (str)
        - mean (float)
        - std (float)
        '''
        self.name = name
        self.mean = mean
        self.std = std

    def __repr__(self):
        pass

    def punch(self):
        '''Returns a powerful punch based on a normal distribution
        '''
        p = max(round(random.normalvariate(self.mean, self.std)), 0)
        return p

class Fighter:
    def __init__(self, left, right):
        self.hp = 100
        self.right = right
        self.left = left

    def __repr__(self):
        pass

    def punch(self, arm='right'):
        if arm == 'right':
            return self.right.punch()
        else:
            return self.left.punch()

class EasyFighter(Fighter):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.hp = 200

    def punch(self, arm='right'):
        return super().punch(arm) + 10

    def regenerate(self):
        self.hp += 5

# inistantiating a bunch of arms

bubb = Arm('Bubb', 10, 4)
dragon = Arm('Dragon', 15, 15)
blorb = Arm('Blorb', 8, 1)
boomerang = Arm('Boomerang', 11, 6)

# creating a bunch of characters

max_brass = Fighter(bubb, dragon)
twintelle = Fighter(blorb, boomerang)
ninjara = EasyFighter(bubb, dragon)

# play with the characters

punch = ninjara.punch()
twintelle.hp -= punch
twintelle.hp

# The original Problem

class Box:

    def __init__(self, size, weight, contents):
        self.size = size
        self.weight = weight
        self.contents = contents

    def __repr__(self):
        return f'Box("{self.size}", {self.weight}, "{self.contents}")'

    def unwrap(self):
        c = self.contents
        self.contents = None
        return c

a_box = Box('big', 5, 'coat')
a_box.contents
a_box.unwrap()
a_box.contents

b_box = Box('medium', 3, 'Bad Lego')
b_box
