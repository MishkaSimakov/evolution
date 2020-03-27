from random import randrange
import math
from Eval2.functions import status
from Eval2.DNA import DNA


class Cell:
    cells = []
    window = ""

    def __init__(self, window, parent=""):
        self.age = 0

        self.energy = 100
        self.devide_energy = 120

        self.max_age = 1000
        self.pain = False
        self.direction = randrange(0, 4)

        self.action_num = 0

        if parent == "":
            self.x = randrange(0, window.width)
            self.y = randrange(0, window.height)

            self.dna = DNA()
        else:
            self.x = parent.x
            self.y = parent.y

            self.dna = DNA(parent)

    def step(self, map):
        self.age += 1

        sts = status(self.x, self.y, self.direction, map)

        if self.energy >= self.devide_energy and sts != "none" and not self.pain:
            sts = "devide"

        if self.pain:
            action = self.dna.pain[self.pain][sts]
        elif self.energy >= self.devide_energy and sts == "none":
            action = 7
        else:
            action = self.dna.action[self.action_num][sts]
            self.action_num = (self.action_num + 1) % 5

        map = self.action(action, map)

    def action(self, action, map):
        if self.direction == 0:
            goal_x = self.x + 1
            goal_y = self.y
        elif self.direction == 1:
            goal_x = self.x
            goal_y = self.y + 1
        elif self.direction == 2:
            goal_x = self.x - 1
            goal_y = self.y
        elif self.direction == 3:
            goal_x = self.x
            goal_y = self.y - 1

        if action == 0:
            if map[self.x + 1][self.y] == 0:
                self.x += 1
                self.direction = 0

                map[self.x][self.y] = self
        elif action == 1:
            if map[self.x][self.y + 1] == 0:
                self.y += 1
                self.direction = 1

                map[self.x][self.y] = self
        elif action == 2:
            if map[self.x - 1][self.y] == 0:
                self.x -= 1
                self.direction = 2

                map[self.x][self.y] = self
        elif action == 3:
            if map[self.x][self.y - 1] == 0:
                self.y -= 1
                self.direction = 3

                map[self.x][self.y] = self
        elif action == 4:
            # if isinstance(map[goal_x][goal_y])
            

        return map

    @classmethod
    def all(cls):
        return cls.cells

    def die(self):
        self.__class__.cells.remove(self)

        del self
