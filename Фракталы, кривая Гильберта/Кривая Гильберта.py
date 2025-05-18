import turtle

# === Глобальные переменные ===
step_count = 0
total_steps = 1

# Цвет по шагу (чем дальше — тем ярче)
def get_color_by_progress(current, total):
    t = current / total
    return (t, 0.4, 1 - t)  # от синего к фиолетовому к красному

# Кривая Гильберта
def hilbert(t, level, angle, step, max_level):
    global step_count, total_steps

    if level == 0:
        return

    t.right(angle)
    hilbert(t, level - 1, -angle, step, max_level)

    t.pencolor(get_color_by_progress(step_count, total_steps))
    t.forward(step)
    step_count += 1

    t.left(angle)
    hilbert(t, level - 1, angle, step, max_level)

    t.pencolor(get_color_by_progress(step_count, total_steps))
    t.forward(step)
    step_count += 1

    hilbert(t, level - 1, angle, step, max_level)

    t.left(angle)
    t.pencolor(get_color_by_progress(step_count, total_steps))
    t.forward(step)
    step_count += 1

    hilbert(t, level - 1, -angle, step, max_level)
    t.right(angle)

# Рисование
def draw_hilbert_curve(order, step=10):
    global step_count, total_steps

    step_count = 0
    total_steps = (2 ** order) ** 2 - 1  # длина пути

    screen = turtle.Screen()
    screen.title(f"Кривая Гильберта — глубина {order}")
    screen.bgcolor("white")

    turtle.colormode(1.0)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    size = step * (2 ** order - 1)
    t.penup()
    t.goto(-size // 2, size // 2)
    t.pendown()

    hilbert(t, order, 90, step, order)

    t.hideturtle()
    screen.mainloop()

# Запуск
depth = int(input("Введите глубину рекурсии (например, 1–6): "))
draw_hilbert_curve(depth)