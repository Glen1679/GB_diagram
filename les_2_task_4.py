# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
el_sum = 0

def func(n):
    global el_sum
    if n == 0:
        return el_sum
    el = 1 / (-2) ** (n - 1)
    el_sum += el
    return func(n - 1)

print(func(int(input('Введите количество эллементов n: '))))
