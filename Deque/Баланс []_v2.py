from collections import deque
import os


def check_brackets_balance(filename):
    """
    Проверяет баланс квадратных скобок в файле.
    Возвращает кортеж (статус, ошибка), где:
    - статус: True/False
    - ошибка: (строка, позиция, тип_ошибки) или None
    """
    stack = deque()
    line_num = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_num += 1
                char_num = 0

                for char in line:
                    char_num += 1
                    if char == '[':
                        stack.append((line_num, char_num))
                    elif char == ']':
                        if not stack:
                            return (False, (line_num, char_num, "Лишняя закрывающая скобка"))
                        stack.pop()

    except FileNotFoundError:
        return (False, None)

    if stack:
        first_unclosed = stack[0]
        return (False, (*first_unclosed, "Незакрытая скобка"))

    return (True, None)


def create_test_file(filename, content):
    """Создает тестовый файл с указанным содержимым"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Создан тестовый файл: {filename}")


def main():
    # Создаем тестовые файлы
    create_test_file("correct.txt", """
begin
    a := [1, 2, [3, 4]];
    if a[0] > 0 then
        b := [[5, 6], 7];
    end;
end
""")

    create_test_file("unclosed.txt", """
begin
    a := [1, 2, [3, 4]];
    if a[0] > 0 then
        b := [5, 6;
    end;
end
""")

    create_test_file("extra_close.txt", """
begin
    a := [1, 2, [3, 4]]];
    if a[0] > 0 then
        b := [5, 6]];
    end;
end
""")

    # Проверяем все созданные файлы
    for filename in ["correct.txt", "unclosed.txt", "extra_close.txt"]:
        print(f"\nПроверка файла {filename}:")
        result, error = check_brackets_balance(filename)

        if result:
            print("✓ Все скобки сбалансированы")
        else:
            if error:
                line, pos, err_type = error
                print(f"× Ошибка в строке {line}, позиция {pos}: {err_type}")

                # Показываем проблемную строку
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if line <= len(lines):
                        print(f"Строка с ошибкой: {lines[line - 1].strip()}")
                        print(" " * (pos - 1) + "^")  # Указатель на позицию ошибки
            else:
                print("× Файл не найден")

    # Удаляем тестовые файлы (опционально)
    if input("\nУдалить тестовые файлы? (y/n): ").lower() == 'y':
        for filename in ["correct.txt", "unclosed.txt", "extra_close.txt"]:
            try:
                os.remove(filename)
                print(f"Файл {filename} удален")
            except FileNotFoundError:
                pass


if __name__ == "__main__":
    main()