from random import randrange
from graphics import GraphWin

def mutate(value, offset):
    if randrange(1, 4) == 1:
        mutate_value = value + (randrange(-offset * 100, offset * 100) / 100)
        if mutate_value != 0:
            return mutate_value
        return mutate_value + 0.01

    return value


def log(data, time, window: GraphWin):
    sum_speed = 0
    sum_satiety = 0
    sum_devide_satiety = 0
    sum_child_count = 0

    for c in data['cells']:
        sum_speed += c.speed
        sum_satiety += c.satiety
        sum_devide_satiety += c.devide_satiety
        sum_child_count += c.childCount

    # print("Количество: ", len(data['cells']))
    # print("Средняя скорость: ", str(sum_speed / len(data['cells'])))
    # print("Средняя сытость: ", str(sum_satiety / len(data['cells'])))
    # print("Средняя сытость для размножения: ", str(sum_devide_satiety / len(data['cells'])))
    # print("_________________")

    x = (time + 10) % window.width

    y1 = 165 - len(data['cells']) / 8
    y2 = 330 - (sum_speed / len(data['cells']) * 20)
    y3 = 495 - len(data['food']) / 4
    y4 = 660 - sum_child_count / len(data['cells']) * 5
    # y4 = 660 - sum_devide_satiety / len(data['cells'])

    window.create_rectangle(x, y1, x + 2, y1 + 2)
    window.create_rectangle(x, y2, x + 2, y2 + 2)
    window.create_rectangle(x, y3, x + 2, y3 + 2)
    window.create_rectangle(x, y4, x + 2, y4 + 2)