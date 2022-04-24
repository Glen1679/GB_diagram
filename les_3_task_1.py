# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
import random

my_list = [random.randint(2, 99) for i in range(100)]
print(my_list)

for i in range(2, 10):
      temp_list = [el for el in my_list if el % i == 0]
      print(f'Следующие числа кратны {i}: {temp_list}')
