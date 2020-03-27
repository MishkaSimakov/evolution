from Eval3.Segment import Segment
from random import randrange
from Eval3.const import *


class Snake:
    def __init__(self, segments):
        self.segments = segments
        # варианты движения
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # инициируем направление движения
        self.vector = self.mapping["Right"]
        self.score = 0

        self.brain = [0] * 5

        for brain_row in range(0, 5):
            self.brain[brain_row] = [(randrange(-100, 100) / 10), (randrange(-100, 100) / 10), (randrange(-100, 100) / 10), (randrange(-100, 100) / 10), (randrange(-100, 100) / 10)]

    def move(self, c):
        """ Движение змейки в заданном направлении"""
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                 x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

    def add_segment(self, c):
        self.score += 1

        """ Добавляем сегмент змейки """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y, c))