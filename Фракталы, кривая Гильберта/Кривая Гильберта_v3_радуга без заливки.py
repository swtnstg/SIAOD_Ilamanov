import turtle
import colorsys  # для HSV → RGB

#Глобальные переменные
step_count = 0
total_steps = 1

#Получить цвет по прогрессу — радужный (через HSV)
def get_rainbow_color(step_index, total_steps):
    hue = step_index / total_steps  # от 0.0 до 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # максимальная насыщенность и яркость
    return (r, g, b)

#Рекурсивная кривая Гильберта
def hilbert(t, level, angle, step, max_level):
    global step_count, total_steps

    if level == 0:
        return

    t.right(angle)
    hilbert(t, level - 1, -angle, step, max_level)

    t.pencolor(get_rainbow_color(step_count, total_steps))
    t.forward(step)
    step_count += 1
    turtle.update()  # обновляем экран вручную (анимация)

    t.left(angle)
    hilbert(t, level - 1, angle, step, max_level)

    t.pencolor(get_rainbow_color(step_count, total_steps))
    t.forward(step)
    step_count += 1
    turtle.update()

    hilbert(t, level - 1, angle, step, max_level)

    t.left(angle)
    t.pencolor(get_rainbow_color(step_count, total_steps))
    t.forward(step)
    step_count += 1
    turtle.update()

    hilbert(t, level - 1, -angle, step, max_level)
    t.right(angle)

#Рисование всей кривой
def draw_hilbert_curve(order, step=10):
    global step_count, total_steps

    step_count = 0
    total_steps = (2 ** order) ** 2 - 1  # путь

    screen = turtle.Screen()
    screen.title(f"🌈 Кривая Гильберта — глубина {order}")
    screen.bgcolor("white")
    turtle.colormode(1.0)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    # Ускоряем отрисовку
    turtle.tracer(0, 0)  # отключает автообновление экрана

    # Центрирование
    size = step * (2 ** order - 1)
    t.penup()
    t.goto(-size // 2, size // 2)
    t.pendown()

    hilbert(t, order, 90, step, order)

    t.hideturtle()
    turtle.update()  # последнее обновление экрана
    screen.mainloop()

#Запуск
depth = int(input("Введите глубину (1–7): "))
draw_hilbert_curve(depth)