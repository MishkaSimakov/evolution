from Eval3.const import *


class Segment:
    """ Сегмент змейки """

    def __init__(self, x, y, c):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="white")