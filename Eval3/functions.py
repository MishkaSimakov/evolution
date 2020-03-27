from tkinter import Canvas


def check_alive(c: Canvas, snake):
    head_coords = c.coords(snake.segments[-1].instance)
    width = c.winfo_width()
    height = c.winfo_height()

    x1, y1, x2, y2 = head_coords
    # проверяем на столкновения с границами игрового поля
    if x2 > width or x1 < 0 or y1 < 0 or y2 > height:
        return False

    # поедание себя
    else:
        for index in range(len(snake.segments) - 1):
            if head_coords == c.coords(snake.segments[index].instance):
                IN_GAME = False

    return True
