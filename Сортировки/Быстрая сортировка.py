#Сортировка вставкой
import random
from datetime import datetime

arr = []
print('Пустой массив: ', arr)

for i in range(10000):
    arr.append(random.randint(10,1000000))
    #print(arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # базовый случай: массив из 0 или 1 элемента уже отсортирован

    pivot = arr[0]  # опорный элемент (обычно первый)
    left = [x for x in arr[1:] if x < pivot]      # элементы меньше опорного
    right = [x for x in arr[1:] if x >= pivot]    # элементы больше или равны опорному

    return quick_sort(left) + [pivot] + quick_sort(right)

start = datetime.now()
arr = quick_sort(arr)
end = datetime.now()

print('Начало сортировки массива:', start)
print('Конец сортировки массива:', end)
print('Отсортированный массив:\n',arr)