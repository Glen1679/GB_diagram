# # задание 9
# num = int(input('Загадайте число: '))
# at_counter =0
#
# while True:
#     pred_num = int(input('Введите число: '))
#     at_counter += 1
#     if pred_num > num:
#         print('Число больше, чем нужно. Попробуйте ещё раз!')
#     elif pred_num < num:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')
#     else:
#         print(f'Вы угодали! Число попыток: {at_counter}')
#         break
#
# 8 задание
#
# deposit_sum = int(input('Введите сумму депозита: '))
# interest_rate = int(input('Введите процентную ставку в формате **% годовых: '))
# needed_sum = int(input('Введите необходимую сумму: '))
# year_counter = 0
#
# while needed_sum > deposit_sum:
#     deposit_sum *= 1 + (interest_rate / 100)
#     year_counter += 1
#
# print(f'Необходимая сумма будет достигнута через {year_counter} лет')

# 10 задание
import random

my_num = int(input('Загадайте число от 1 до 100: '))
min = 1
max = 100

while True:
    print(min)
    print(max)
    computer_number = random.randint(min, max)
    print(computer_number)
    action = int(input('Число компьютера 1 — равно, 2 — больше, 3 — меньше: '))
    if action == 2:
        max -= max - computer_number
    elif action == 3:
        min += computer_number - min
    elif action == 1:
        print('Победа')
        break
    else:
        continue