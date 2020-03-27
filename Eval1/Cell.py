import random
import math
from Eval1.functions import mutate


class Cell:
    cells = []

    def __init__(self, parent=""):
        self.parent = parent
        self.age = 1

        if isinstance(self.parent, Cell):
            self.x = mutate(self.parent.x, 0.1)
            self.y = mutate(self.parent.y, 0.1)

            self.speed = mutate(self.parent.speed, 1)
            self.devide_satiety = mutate(self.parent.devide_satiety, 10)
            self.satiety = self.parent.devide_satiety / self.parent.childCount
            self.childCount = math.ceil(abs(mutate(self.parent.childCount, 4)))
        else:
            self.x = random.randrange(0, 500)
            self.y = random.randrange(0, 500)

            self.speed = random.randrange(50, 200) / 100
            self.devide_satiety = 125
            self.satiety = 100
            self.childCount = 3

        self.move_cost = 1.15

        # self.figure = Circle(Point(self.x, self.y), 5)
        # self.figure.setFill('red')

        self.__class__.cells.append(self)

    def move(self, all_food):
        self.age += 1

        nearest_distance = math.inf
        nearest_food = ""

        for food in all_food:
            distance = math.sqrt((self.x - food.x) ** 2 + (self.y - food.y) ** 2)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_food = food

        if nearest_distance <= self.speed:
            self.x = nearest_food.x
            self.y = nearest_food.y

            self.satiety -= self.full_move_cost() * (nearest_distance / self.speed)

            self.satiety += nearest_food.cost
            nearest_food.eat()
        else:
            k = nearest_distance / self.speed

            vertical_distance = nearest_food.y - self.y
            horizontal_distance = nearest_food.x - self.x

            self.x += horizontal_distance / k
            self.y += vertical_distance / k

            self.satiety -= self.full_move_cost()

        if self.satiety <= 0:
            self.die()

        if self.satiety >= self.devide_satiety:
            for i in range(0, self.childCount):
                Cell(self)

            self.satiety -= self.devide_satiety / self.childCount

        # self.figure.move(self.x, self.y)

    @classmethod
    def all(cls):
        return cls.cells

    def die(self):
        # self.figure.undraw()
        self.__class__.cells.remove(self)

        del self

    def full_move_cost(self):
        return (self.move_cost ** (self.speed * 2)) * (self.age / 100)
