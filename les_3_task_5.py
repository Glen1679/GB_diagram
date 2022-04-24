#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random

my_list = [random.randint(-100, 100) for i in range(100)]
print(my_list)

negative_max = -1000

for el in my_list:
    temp = 0
    if el < 0:
        if el > negative_max:
            negative_max = el
print(f'Максимальный отрицательный элемент массива: {negative_max} находится на позиции {my_list.index(negative_max)} ')

