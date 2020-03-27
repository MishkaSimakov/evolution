from tkinter import *
import random
from Eval3.Segment import Segment
from Eval3.Snake import Snake
from Eval3.functions import *
from Eval3.Food import Food

# переменные
from Eval3.const import *

# map = [0] *
#
# for brain_row in range(0, 5):
#     self.brain[brain_row] =


def main():
    global food

    if check_alive(c, snake):
        snake.move(c)
        head_coords = c.coords(snake.segments[-1].instance)

        # поедание яблока
        if head_coords == food.position():
            snake.add_segment(c)

            food.eat()

            # food = Food(c)

        root.after(100, main)
    else:
        print("end")


# настройки окна
root = Tk()
root.title("Snake")

c = Canvas(root, width=width, height=height, bg="#003300")
c.grid()

root.update()

# создаем сегменты и саму змейку
segments = [Segment(SEG_SIZE, SEG_SIZE, c),
            Segment(SEG_SIZE * 2, SEG_SIZE, c),
            Segment(SEG_SIZE * 3, SEG_SIZE, c)]

Food(c)
snake = Snake(segments)

main()
root.mainloop()