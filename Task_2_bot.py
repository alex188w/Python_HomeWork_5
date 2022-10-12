# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет 
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

print('Здравствуйте! Я бот-Инт. Предлагаю Вам сыграть в игру "Матеметика в конфетах"')
name_player = input('Назовите, пожалуйста, свое имя: ')
num_player = randint(1, 2)
if num_player == 1:
    print('По жребию я, бот-Инт, начинаю игру первым')
else:
    print(f'По жребию Вы, {name_player} начинаете игру первым')

number_cand = int(165) # для уменьшения количества итераций, для проверки, взято количество конфет - 165, смысл игры оостается тот же

dif = 0
while number_cand > 0:
    if not num_player % 2:
        print(f'На столе лежит {number_cand} конфет(-а).')
        dif = int(input(f'{name_player} - возьмите необходимое количество конфет (не более 28): '))
        if 0 < dif < 29:
            number_cand = number_cand - dif
            num_player += 1
        else:
            print(f'{name_player} - вы берете количество конфет не по условию. Вы - проиграли!')
            break
        if number_cand < 0:
            number_cand = number_cand + dif
            num_player -= 1
            print(f'{name_player} - на столе всего {number_cand} конфет. ')
            dif = int(input('Возьмите количество конфет не более этого: '))
            number_cand = number_cand - dif
            num_player += 1
        if number_cand == 0:
            print(f'{name_player} - поздравляю! Вы - выиграли!! Все конфеты - Ваши!!!')
            
    else:
        print(f'На столе лежит {number_cand} конфет(-а).')
        if number_cand >27:
            dif = randint(1, 28)
        else:
            dif = randint(1, number_cand)
        print(f'Я, бот-Инт, беру {dif} конфет')
        number_cand = number_cand - dif
        num_player += 1
        
        if number_cand == 0:
            print('Я, бот-Инт, поздравляю себя! Я - выиграл!! Все конфеты - мои!!!')
            