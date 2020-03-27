from graphics import *
from Eval1.Cell import Cell
from Eval1.Food import Food
from Eval1.functions import log
import time


# window = GraphWin("Evolution", 500, 500)

# chart
chart_width = 1750

chart = GraphWin("Chart", chart_width, 665)
chart.create_line(10, 0, 10, 665)
chart.create_line(0, 165, chart_width, 165)
chart.create_line(0, 330, chart_width, 330)
chart.create_line(0, 495, chart_width, 495)
chart.create_line(0, 660, chart_width, 660)

chart.create_text(100, 10, text="Количество клеток")
chart.create_text(100, 175, text="Скорость")
chart.create_text(100, 340, text="Количество еды")
chart.create_text(100, 505, text="Количество потомства")

for i in range(0, 100):
    Food()

for i in range(0, 100):
    Cell()

step = 0

while True:
    for i in range(0, 10):
        Food()

    if step % 10 == 0:
        log({
            'cells': Cell.all(),
            'food': Food.all()
        }, step / 5, chart)

    print(len(Cell.all()))
    time.sleep(0.01)

    for cell in Cell.all():
        cell.move(Food.all())

    update(100)

    step += 1
