# 4. Определить, какое число в массиве встречается чаще всего.

import random

my_list = [random.randint(0, 10) for i in range(30)]
print(my_list)

counter = [0, 0]
for el in my_list:
    current_count = 0
    for i in my_list:
        if el == i:
            current_count += 1
    if current_count > counter[1]:
        counter[1] = current_count
        counter[0] = el
print(f'Число {counter[0]} встречается в массиве чаще всего ({counter[1]} раз(а))')