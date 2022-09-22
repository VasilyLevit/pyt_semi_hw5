# Создайте программу для игры с конфетами человек против человек.
# Условие задачи: На столе лежиит 2021 конфета. Играют 2а игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За одни ход можно забрать # не более чем 28 конфет. 
# Все конфеты оппонета достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игрок, чтобы забрать все конфеты у своего конкурента?
# а) Добавьте игру против бота
# б) Подумайте как наделить бота "интеллектом"

import random

def game_strategy(total_sweets, max):
    cicle_sweets = max + 1
    if (total_sweets % cicle_sweets) != 0:
        return total_sweets % cicle_sweets
    else:
        return random.randint(1, max + 1)

def input_gamer(max):
    gamer_sweets = int(input('Ты взял: '))
    if 0 < gamer_sweets <= max:
        return gamer_sweets
    else:
        return input_gamer

print('*' * 5, 'Игра с конфетами', '*' * 5)
var_viel = -1, 1
first_move = random.choice(var_viel)
count_sweets = 100
max_sweets = 28
print('Всего конфет: ', count_sweets)
while count_sweets > 0:
    if first_move == 1:
        count_sweets -= input_gamer(max_sweets)
        win = 0
    else:
        take_sweets = game_strategy(count_sweets, max_sweets)
        count_sweets -= take_sweets
        print('Игрок 2 взял: ', take_sweets)
        win = 1
    first_move *= -1
    print('Осталось', count_sweets, 'конфет')

if win == 0:
    print('Ты победил !!!')
else:
    print('Победил игрок 2 !!!')

print('Game over') 