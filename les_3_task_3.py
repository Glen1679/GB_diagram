#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

my_list = [random.randint(-100, 100) for i in range(30)]
print(my_list)

# не понял как решить это задание без поиска максимального и минимального элементов

max = 0
min = 0

for el in my_list:
    if el > max:
        max = el
    if el < min:
        min = el
print(max, min)

max_index = my_list.index(max)
min_index = my_list.index(min)

my_list[max_index], my_list[min_index] = my_list[min_index], my_list[max_index]
print(my_list)


