def result ():
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    city = input('Введите город: ')
    print('{}, {} год(а), проживает в городе {}'.format(name,age, city))

#result()

def maximum (*args):
    print(max(*args))

#maximum(1,2,3,4)
import random
player_name = input('Input player name: ')
player_health = int(input('Input player health: '))
enemy_name = 'Hunter'
enemy_health = 100


player = {'name': player_name, 'health': player_health, 'damage': random.randint(1,50)}
enemy = {'name': enemy_name, 'health': enemy_health, 'damage': random.randint(1,50)}

tern= {'1' : 'player','2':'enemy'}

print(player['health'])
print(enemy['health'])

def atack (person1,person2):
    person1['health']=person1['health'] - person2['damage']


while True:
    wh_tern = random.randint(1, 2)
    if(wh_tern == 1):
        print('{} атакован {}'.format(player['name'],enemy['name']))
        atack(player,enemy)
        print('У {} осталось {} здоровья'.format(player['name'], player['health']))
        if(player['health']<=0):
            print('{} Убит'.format(player['name']))
            break
    else:
        print('{} атакован {}'.format(enemy['name'], player['name']))
        atack(enemy,player)
        print('У {} осталось {} здоровья'.format(enemy['name'], enemy['health']))
        if(enemy['health']<=0):
            print('{} Убит'.format(enemy['name']))
            break



#print(player['health'])
#player['health']=player['health'] - enemy['damage']
#print(player['health'])