"""
**Базова концепція:**
1. При запуску файлу game.py запропонувати користувачу ввести своє ім'я.
2. Запропонувати користувачу ввести **start** для початку гри.
3. Хід починається з атаки гравця:
   1. гравець обирає чаклуна(1), воїна(2) чи розбійника(3).
   2. Вибір противника обирається автоматично.
   3. Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна.
   4. Після атаки вивести результат атаки - влучив, промахнувся, нічия. Нічия у випадку, якщо обрані однакові класи.
   5. Далі атакує противник, користувач обирає захист - механізм той самий.
4. Після успішної атаки у противника зменшуеться кількість життів. Гравець отримує 1 очко.
5. Після невдалого захисту гравець втрачає одне життя.
6. Коли у гравця закінчуються життя - ігра завершується.
7. Коли у противника закінчуються життя - гравець отримує додатково +5 очків і генерується новий противник.
8. При завершенні гри вивести результат на екран.
"""


import sys
from models import Enemy
from models import Player
from game_exceptions import GameOver
from game_exceptions import EnemyDown
import settings


def play():
    s_inp = input("Enter 'start' to play: ")
    if s_inp.lower() == 'start':
        name = input('Enter your name: ')
        player1 = Player(name, level=1)
        enemy_obj = Enemy(level=1, lives=1)
        level = 1
        while True:
            try:
                print('------------------------------------------------')
                player1.attack()
                player1.defence()
            except EnemyDown:
                print('Enemy is Down! Get ready for the next one!')
                player1.score += 5
                level += 1
                enemy_obj1 = Enemy(level=level, lives=level)
                print(f'Your enemy has {enemy_obj1.lives} lives, {enemy_obj1.level} level')
    elif s_inp.lower() == 'help':
        settings.do_work()
        command = input("Enter your command: ")
        if command.lower() == 'score':
            settings.show_score()
        if command.lower() == 'exit':
            sys.exit()
    else:
        input("Enter 'start' to play: ")


if __name__ == '__main__':
    try:
        play()
    except GameOver as err:
        if err.score > 0:
            with open('scores.txt', 'a', encoding="utf8") as file:
                file.write(f'PLAYER: {err.name} | SCORE: {err.score}\n')
        print(f'\nThe Game is Over. Your score is {err.score}.')
    except KeyboardInterrupt as er:
        pass
    finally:
        print('\nGoodbye!')
