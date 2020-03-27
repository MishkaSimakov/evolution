import random


class Food:
    food = []

    def __init__(self):

        self.x = random.randrange(0, 500)
        self.y = random.randrange(0, 500)

        self.cost = 25

        # self.figure = Rectangle(Point(self.x, self.y), Point(self.x + self.cost / 5, self.y + self.cost / 5))
        # self.figure.setFill('blue')

        self.__class__.food.append(self)

    @classmethod
    def all(cls):
        return cls.food

    def eat(self):
        # self.figure.undraw()
        self.__class__.food.remove(self)

        del self
