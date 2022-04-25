import random
def game():
    number=random.randint(1,100)
    print(number)

    action = None

    while True:
        action = input('Действие: ')
        if action == '>':
            number = number + random.randint(1,100-number)
            print(number)
        elif action == '<':
            number = number - random.randint(1,number)
            print(number)
        elif action == '=':
            print('Победа')
            break
