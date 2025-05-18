#Сортировка вставкой
import random
from datetime import datetime

arr = []
print('Пустой массив: ', arr)

for i in range(10000):
    arr.append(random.randint(10,1000000))
    #print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]               # текущий элемент, который будем вставлять
        j = i - 1                  # индекс последнего элемента отсортированной части

        # Пока j >= 0 и элемент слева больше key — сдвигаем элемент вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]    # сдвигаем элемент вправо
            j -= 1

        # Вставляем key на нужное место
        arr[j + 1] = key

    return arr
start = datetime.now()
arr = insertion_sort(arr)
end = datetime.now()

print('Начало сортировки массива:', start)
print('Конец сортировки массива:', end)
print('Отсортированный массив:\n',arr)