import turtle
import colorsys

#Глобальные переменные
step_count = 0
total_steps = 1
cell_size = 10  # Размер одной зоны для заливки

#Радужный цвет по индексу
def get_rainbow_color(step_index, total_steps):
    hue = step_index / total_steps
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

#Функция заливки зоны вокруг текущей позиции
def fill_zone(t, color, size):
    # Сохраняем позицию и угол
    pos = t.pos()
    heading = t.heading()

    t.fillcolor(color)
    t.begin_fill()

    t.penup()
    t.setheading(0)
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.right(90)
    t.pendown()

    for _ in range(4):
        t.forward(size)
        t.right(90)

    t.end_fill()

    # Возвращаемся назад
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()


#Рекурсивная кривая Гильберта
def hilbert(t, level, angle, step, max_level):
    global step_count, total_steps, cell_size

    if level == 0:
        return

    t.right(angle)
    hilbert(t, level - 1, -angle, step, max_level)

    color = get_rainbow_color(step_count, total_steps)
    fill_zone(t, color, cell_size)
    t.pencolor(color)
    t.forward(step)
    step_count += 1
    turtle.update()

    t.left(angle)
    hilbert(t, level - 1, angle, step, max_level)

    color = get_rainbow_color(step_count, total_steps)
    fill_zone(t, color, cell_size)
    t.pencolor(color)
    t.forward(step)
    step_count += 1
    turtle.update()

    hilbert(t, level - 1, angle, step, max_level)

    t.left(angle)
    color = get_rainbow_color(step_count, total_steps)
    fill_zone(t, color, cell_size)
    t.pencolor(color)
    t.forward(step)
    step_count += 1
    turtle.update()

    hilbert(t, level - 1, -angle, step, max_level)
    t.right(angle)

#Главная функция
def draw_hilbert_curve(order, step=10):
    global step_count, total_steps, cell_size

    step_count = 0
    total_steps = (2 ** order) ** 2 - 1
    cell_size = step

    screen = turtle.Screen()
    screen.title(f"🌈 Кривая Гильберта с заливкой — глубина {order}")
    screen.bgcolor("white")
    turtle.colormode(1.0)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    turtle.tracer(0, 0)

    size = step * (2 ** order - 1)
    t.penup()
    t.goto(-size // 2, size // 2)
    t.setheading(0)
    t.pendown()

    hilbert(t, order, 90, step, order)

#Запуск
depth = int(input("Введите глубину (1–7): "))
draw_hilbert_curve(depth)
