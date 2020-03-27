from Eval3.const import *
from tkinter import Canvas
from random import randint


class Food:
    def __init__(self, c: Canvas):
        self.pos_x = SEG_SIZE * randint(1, (width - SEG_SIZE) / SEG_SIZE)
        self.pos_y = SEG_SIZE * randint(1, (height - SEG_SIZE) / SEG_SIZE)
        self.figure = c.create_rectangle(self.pos_x, self.pos_y,
                                   self.pos_x + SEG_SIZE, self.pos_y + SEG_SIZE,
                                   fill="red", tag="food")

        self.c = c

    def eat(self):
        self.c.delete(self.figure)

        del self

    def position(self):
        return self.c.coords(self.figure)