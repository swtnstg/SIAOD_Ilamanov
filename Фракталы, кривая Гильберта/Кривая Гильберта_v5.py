import turtle
import colorsys

#Глобальные переменные
step_count = 0
total_steps = 1
cell_size = 10
draw_mode = "smooth"  # fast / smooth / step
t = None  # глобальная черепаха

#Цвет по радуге
def get_rainbow_color(step_index, total_steps):
    hue = step_index / total_steps
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

#Заливка зоны
def fill_zone(t, color, size):
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
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

#Рекурсивная кривая
def hilbert(t, level, angle, step, max_level):
    global step_count, total_steps, cell_size

    if level == 0:
        return

    t.right(angle)
    hilbert(t, level - 1, -angle, step, max_level)

    draw_step(t, step)
    t.left(angle)
    hilbert(t, level - 1, angle, step, max_level)

    draw_step(t, step)
    hilbert(t, level - 1, angle, step, max_level)

    t.left(angle)
    draw_step(t, step)
    hilbert(t, level - 1, -angle, step, max_level)
    t.right(angle)

#Один шаг
def draw_step(t, step):
    global step_count, total_steps, draw_mode

    color = get_rainbow_color(step_count, total_steps)
    fill_zone(t, color, cell_size)
    t.pencolor(color)
    t.forward(step)
    step_count += 1

    if draw_mode == "step":
        turtle.update()
    elif draw_mode == "smooth" and step_count % 500 == 0:
        turtle.update()

#Обработка кликов по экрану
def click_handler(x, y):
    global draw_mode
    if draw_mode == "fast":
        draw_mode = "smooth"
        print("→ Режим: smooth")
    elif draw_mode == "smooth":
        draw_mode = "step"
        print("→ Режим: step")
    else:
        draw_mode = "fast"
        print("→ Режим: fast")

#Сохранение изображения
def save_canvas():
    canvas = turtle.getcanvas()
    canvas.postscript(file="hilbert_output.eps")
    print("💾 Изображение сохранено как 'hilbert_output.eps'")

# 🎨 Запуск
def draw_hilbert_curve(order, step=10, mode="smooth"):
    global step_count, total_steps, cell_size, draw_mode, t

    step_count = 0
    total_steps = (2 ** order) ** 2 - 1
    cell_size = step
    draw_mode = mode

    screen = turtle.Screen()
    screen.title(f"🌈 Кривая Гильберта — глубина {order} (клик для смены режима)")
    screen.bgcolor("white")
    turtle.colormode(1.0)
    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    # Центрирование
    size = step * (2 ** order - 1)
    t.penup()
    t.goto(-size // 2, size // 2)
    t.setheading(0)
    t.pendown()

    screen.onclick(click_handler)  # клик по экрану — переключение режима
    screen.onkey(save_canvas, "s")  # клавиша "s" — сохранить
    screen.listen()

    hilbert(t, order, 90, step, order)

    t.hideturtle()
    turtle.update()
    screen.mainloop()

# 🚀 Интерфейс запуска
depth = int(input("Введите глубину (1–6): "))
print("Начальный режим: smooth. Кликни по экрану, чтобы переключать.")
print("Нажми 's' во время рисования, чтобы сохранить как .eps")

draw_hilbert_curve(depth, step=10, mode="smooth")
