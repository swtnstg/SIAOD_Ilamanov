import random
import time
import bisect


class InterpolationSearch:
    def __init__(self, data=None):
        self.data = sorted(data) if data else []

    def generate_random_data(self, size=1000, min_val=0, max_val=10000):
        """Генерация случайных данных"""
        self.data = sorted(random.randint(min_val, max_val) for _ in range(size))
        print(f"Сгенерировано {size} случайных чисел от {min_val} до {max_val}")

    def add_element(self, x):
        """Добавление элемента с сохранением сортировки"""
        bisect.insort(self.data, x)
        print(f"Добавлен элемент: {x}")

    def remove_element(self, x):
        """Удаление элемента"""
        if x in self.data:
            self.data.remove(x)
            print(f"Удален элемент: {x}")
        else:
            print(f"Элемент {x} не найден")

    def interpolation_search(self, x):
        """Интерполяционный поиск"""
        low, high = 0, len(self.data) - 1

        while low <= high and self.data[low] <= x <= self.data[high]:
            pos = low + ((x - self.data[low]) * (high - low)) // (self.data[high] - self.data[low])
            pos = max(low, min(pos, high))  # Ограничение в пределах диапазона

            if self.data[pos] == x:
                return pos
            elif self.data[pos] < x:
                low = pos + 1
            else:
                high = pos - 1
        return -1

    def binary_search(self, x):
        """Бинарный поиск для сравнения"""
        return bisect.bisect_left(self.data, x) if x in self.data else -1

    def python_search(self, x):
        """Встроенный поиск Python (index)"""
        try:
            return self.data.index(x)
        except ValueError:
            return -1

    def test_search(self, x, num_tests=1000):
        """Тестирование скорости разных методов поиска"""
        print(f"\nПоиск элемента {x} в массиве из {len(self.data)} элементов")

        # Проверяем, существует ли элемент
        exists = x in self.data
        print(f"Элемент {'найден' if exists else 'не найден'} в массиве")

        # Интерполяционный поиск
        start = time.perf_counter()
        for _ in range(num_tests):
            self.interpolation_search(x)
        int_time = time.perf_counter() - start

        # Бинарный поиск
        start = time.perf_counter()
        for _ in range(num_tests):
            self.binary_search(x)
        bin_time = time.perf_counter() - start

        # Встроенный поиск Python
        start = time.perf_counter()
        for _ in range(num_tests):
            self.python_search(x)
        py_time = time.perf_counter() - start

        print("\nСреднее время выполнения (микросекунды):")
        print(f"Интерполяционный поиск: {int_time * 1e6 / num_tests:.2f} мкс")
        print(f"Бинарный поиск:         {bin_time * 1e6 / num_tests:.2f} мкс")
        print(f"Встроенный поиск Python: {py_time * 1e6 / num_tests:.2f} мкс")

        speedup_int = bin_time / int_time if int_time > 0 else 0
        speedup_bin = py_time / bin_time if bin_time > 0 else 0

        print(
            f"\nИнтерполяционный поиск {'медленнее' if speedup_int < 1 else 'быстрее'} бинарного в {max(speedup_int, 1 / speedup_int):.1f} раз")
        print(
            f"Бинарный поиск {'медленнее' if speedup_bin < 1 else 'быстрее'} встроенного в {max(speedup_bin, 1 / speedup_bin):.1f} раз")


def main():
    search = InterpolationSearch()

    while True:
        print("\nМеню:")
        print("1. Сгенерировать случайные данные")
        print("2. Добавить элемент")
        print("3. Удалить элемент")
        print("4. Выполнить поиск элемента")
        print("5. Сравнить алгоритмы поиска")
        print("6. Показать данные")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            size = int(input("Введите размер массива: "))
            min_val = int(input("Минимальное значение: "))
            max_val = int(input("Максимальное значение: "))
            search.generate_random_data(size, min_val, max_val)

        elif choice == "2":
            x = int(input("Введите элемент для добавления: "))
            search.add_element(x)

        elif choice == "3":
            x = int(input("Введите элемент для удаления: "))
            search.remove_element(x)

        elif choice == "4":
            x = int(input("Введите элемент для поиска: "))
            methods = {
                "1": ("Интерполяционный поиск", search.interpolation_search),
                "2": ("Бинарный поиск", search.binary_search),
                "3": ("Встроенный поиск Python", search.python_search)
            }
            print("\nВыберите метод поиска:")
            for key, (name, _) in methods.items():
                print(f"{key}. {name}")

            method = input("Ваш выбор: ")
            if method in methods:
                name, func = methods[method]
                start = time.perf_counter()
                result = func(x)
                elapsed = time.perf_counter() - start

                if result != -1:
                    print(f"\n{name}: элемент найден на позиции {result}")
                else:
                    print(f"\n{name}: элемент не найден")
                print(f"Время выполнения: {elapsed * 1e6:.2f} микросекунд")
            else:
                print("Неверный выбор")

        elif choice == "5":
            x = int(input("Введите элемент для тестирования: "))
            num_tests = int(input("Количество тестов (рекомендуется 1000+): "))
            search.test_search(x, num_tests)

        elif choice == "6":
            print("\nТекущие данные:")
            print(search.data[:20], "...") if len(search.data) > 20 else print(search.data)
            print(f"Всего элементов: {len(search.data)}")

        elif choice == "7":
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()