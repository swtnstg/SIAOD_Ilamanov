import turtle
import colorsys
import time  # Для таймера

# Глобальные переменные
step_count = 0
total_steps = 1
cell_size = 10
draw_mode = "smooth"
t = None
hilbert_calls = 0  # Счётчик вызовов функции hilbert

# Радужный цвет
def get_rainbow_color(step_index, total_steps):
    hue = step_index / total_steps
    return colorsys.hsv_to_rgb(hue, 1, 1)

# Заливка клетки вокруг текущей позиции
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

# Один шаг
def draw_step(t, step, fill_enabled):
    global step_count, total_steps, draw_mode
    color = get_rainbow_color(step_count, total_steps)
    if fill_enabled:
        fill_zone(t, color, cell_size)
    t.pencolor(color)
    t.forward(step)
    step_count += 1
    if draw_mode == "step":
        turtle.update()
    elif draw_mode == "smooth" and step_count % 500 == 0:
        turtle.update()

# Рекурсивная кривая Гильберта
def hilbert(t, level, angle, step, max_level, fill_enabled):
    global hilbert_calls
    hilbert_calls += 1

    if level == 0:
        return
    t.right(angle)
    hilbert(t, level - 1, -angle, step, max_level, fill_enabled)
    draw_step(t, step, fill_enabled)
    t.left(angle)
    hilbert(t, level - 1, angle, step, max_level, fill_enabled)
    draw_step(t, step, fill_enabled)
    hilbert(t, level - 1, angle, step, max_level, fill_enabled)
    t.left(angle)
    draw_step(t, step, fill_enabled)
    hilbert(t, level - 1, -angle, step, max_level, fill_enabled)
    t.right(angle)

# Переключение режима по клику
def click_handler(x, y):
    global draw_mode
    if draw_mode == "fast":
        draw_mode = "smooth"
    elif draw_mode == "smooth":
        draw_mode = "step"
    else:
        draw_mode = "fast"
    print(f"🔁 Режим переключён на: {draw_mode}")

# Сохранение EPS
def save_canvas_as_eps():
    canvas = turtle.getcanvas()
    canvas.postscript(file="hilbert_output.eps")
    print("💾 Сохранено: hilbert_output.eps")

# Главная функция
def draw_hilbert_curve(order, step=None, mode="smooth", fill_enabled=True):
    global step_count, total_steps, cell_size, draw_mode, t, hilbert_calls
    step_count = 0
    hilbert_calls = 0
    total_steps = (2 ** order) ** 2 - 1
    draw_mode = mode

    # Автоматический масштаб
    screen_size = 800
    if step is None:
        step = screen_size // (2 ** order)
    cell_size = step

    turtle.setup(width=screen_size + 50, height=screen_size + 50)
    screen = turtle.Screen()
    screen.title(f"🌈 Кривая Гильберта — глубина {order} — режим: {mode}")
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

    # Управление
    screen.onclick(click_handler)
    screen.onkey(save_canvas_as_eps, "s")
    screen.listen()

    # Таймер начала
    start_time = time.time()

    hilbert(t, order, 90, step, order, fill_enabled)

    # Таймер завершения
    duration = time.time() - start_time
    print(f"⏱ Время отрисовки: {duration:.2f} секунд")
    print(f"🔁 Вызовов функции hilbert: {hilbert_calls}")

    t.hideturtle()
    turtle.update()
    screen.mainloop()

# Запуск
depth = int(input("Введите глубину (1–7): "))
fill_input = input("Включить заливку ячеек? (y/n): ").strip().lower()
fill_enabled = fill_input == "y"

print("🖱 Клик — переключение режима (fast, smooth, step)")
print("💾 Нажми 's' — сохранить в EPS")
draw_hilbert_curve(depth, step=None, mode="smooth", fill_enabled=fill_enabled)