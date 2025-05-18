import random
import time
from datetime import datetime

#Сортировка вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

#Генерация массива
size = 10000
original = [random.randint(1, 100000) for _ in range(size)]

#Сортировка вставкой
arr1 = original.copy()
start = time.time()
insertion_sort(arr1)
end = time.time()
print(f"Insertion sort: {end - start:.6f} сек")

#Быстрая сортировка
arr2 = original.copy()
start = time.time()
arr2 = quick_sort(arr2)
end = time.time()
print(f"Quick sort: {end - start:.6f} сек")

#Стандартная сортировка Python
arr3 = original.copy()
start = time.time()
arr3.sort()  # или sorted(arr3)
end = time.time()
print(f"Built-in sort: {end - start:.6f} сек")