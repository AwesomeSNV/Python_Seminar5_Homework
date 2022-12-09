# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#Player VS Bot

from random import randint, choice

def Move_Input(player):
    invite_messages = ['сколько конфет возьмете от 1 до 28?','Ваша очередь, берите не больше 28 штук!','Не стесняйся, возми конфеты!', 'от одной до двадцати восьми, конфеты бери!']
    error_messages = ['Так не пойдет, нужно взять от 1 до 28 штук', 'Подумай еще, количество не корректно', 'Вспомни правила! От 1 до 28 конфет!']
    x = int(input(f'{player}, {choice(invite_messages)} Сколько конфет возьмете?: \n'))
    while x < 1 or x > 28:
        x = int(input(f'{player}, {choice(error_messages)} Введите правильное количество! \n'))
    return x

def Move_Details(player, n, count, fund):
    print(f'{player} взял со стола {n} конфет, в его копилке сейчас {count} конфет! На столе осталось {fund} конфет!\n')

print(f'Добро пожаловать в игру "Забери все конфеты!"\n'
      'правила игры: На столе лежит некоторое количество конфет,\n'
      'случайным образом определяется кто будет ходить первым.\n'
      'За один ход можно взять со стола не более 28 конфет.\n'
      'Все конфеты оппонента достаются игроку сделавшему последний ход.\n'
      'Приятной игры!\n')

first_player = input('Введите имя первого игрока: \n')
second_player = 'Megatron'
candy_fund = int(input('Введите колличество конфет на столе: \n'))

toss_a_coin = randint(0,2)
if toss_a_coin:
    print(f'Первый ход делает {first_player}\n')
else:
    print(f'Первый ход делает {second_player}\n')

first_player_counter = 0
second_player_counter = 0

while candy_fund > 28:
    if toss_a_coin:
        n = Move_Input(first_player)
        first_player_counter += n
        candy_fund -= n
        toss_a_coin = False
        Move_Details(first_player, n, first_player_counter, candy_fund)
    else:
        n = randint(1,29)
        second_player_counter += n
        candy_fund -= n
        toss_a_coin = True
        Move_Details(second_player, n, second_player_counter, candy_fund)
winner_messages = ['И победитель:','Победа достаётся игроку:', 'Приз в студию! Победитель:']
if toss_a_coin:
    print(f'{choice(winner_messages)} {first_player}!\n')
else:
    print(f'{choice(winner_messages)} {second_player}!\n')