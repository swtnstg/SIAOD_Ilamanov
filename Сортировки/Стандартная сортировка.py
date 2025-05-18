#Сортировка вставкой
import random
from datetime import datetime

arr = []
print('Пустой массив: ', arr)

for i in range(10000):
    arr.append(random.randint(10,1000000))
    #print(arr)

start = datetime.now()
arr = sorted(arr)
end = datetime.now()

print('Начало сортировки массива:', start)
print('Конец сортировки массива:', end)
print('Отсортированный массив:\n',arr)