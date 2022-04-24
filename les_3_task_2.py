#2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа

import random

my_list = [random.randint(2, 99) for i in range(100)]
print(my_list)

# my_list_even_index = [my_list.index(el) for el in my_list if el % 2 == 0]
# print(my_list_even_index)

my_temp_list = []
counter = 0
for el in my_list:
    if el % 2 == 0:
        my_temp_list.append(counter)
    counter += 1
print(my_temp_list)