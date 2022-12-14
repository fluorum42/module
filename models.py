import random
from game_exceptions import EnemyDown
from game_exceptions import GameOver
from settings import LIVES


class Enemy:
    """
    Атрибути класу - level, lives.
    Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.
    """
    def __init__(self, level, lives):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        """
        повертає випадкове число від 1 до 3
        """
        return random.randint(1, 3)

    def decrease_lives(self):
        """
        зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    Конструктор приймає ім'я гравця.
    Кількість життів отримується з settings.
    Рахунок дорівнює нулю
    """
    def __init__(self, name, level, score=0, lives=LIVES):
        self.level = level
        self.name = name
        self.lives = lives
        self.score = score

    @staticmethod
    def fight(attack, defence):
        """
        Чаклун(1) перемагає воїна(2). Воїн(2) перемагає розбійника(3). Розбійник перемагає чаклуна(3).
        повертає результат атаки/захисту:
        0 нічия
        -1 aтака/захист невдалі.
        1 атака/захист вдалі.
        """
        if (attack == 1 and defence == 2) or (attack == 2 and defence == 3) or (attack == 3 and defence == 1):
            return 1
        if (attack == 2 and defence == 1) or (attack == 3 and defence == 2) or (attack == 1 and defence == 3):
            return -1
        if attack == defence:
            return 0

    def decrease_lives(self):
        """
        викликає виняток GameOver
        """
        self.lives -= 1
        if self.lives == 0:
            print('You died! :(')
            raise GameOver(self.score, self.name)

    def attack(self):
        """
        отримує input (1, 2, 3) від користувача;
        обирає атаку противника з об'екту enemy_obj;
        викликає метод fight();
        Якщо результат 0 - вивести "It's a draw!"
        Якщо 1 = "You attacked successfully!" та зменшує кількість життів противника на 1;
        Якщо -1 = "You missed!"
        """
        try:
            player = int(input("Choose your character 1, 2 or 3: "))
            enemy = Enemy.select_attack()
            self.validate_player(player)
            fight_process = self.fight(attack=player, defence=enemy)
            if fight_process == 1:
                self.score = self.score + 1
                print('You attacked successfully!')
                Enemy(level=1, lives=1).decrease_lives()
            if fight_process == -1:
                print('You missed!')
            if fight_process == 0:
                print("It's a draw!")
        except ValueError:
            int(input("You can use only numbers 1, 2 or 3. Try again: "))

    def defence(self):
        """
        такий самий, як метод attack(), тільки в метод fight першим передається атака противника, та при вдалій атаці
        противника викликається метод decrease_lives гравця.
        """
        try:
            enemy = Enemy.select_attack()
            player = int(input("Choose your character 1, 2 or 3: "))
            self.validate_player(player)
            fight_process = self.fight(attack=enemy, defence=player)
            if fight_process == 1:
                self.decrease_lives()
                print("The Enemy strikes!!")
            if fight_process == -1:
                print('You defenced successfully!')
            if fight_process == 0:
                print("It's a draw!")
        except ValueError:
            int(input("You can use only numbers 1, 2 or 3. Try again: "))


    @staticmethod
    def validate_player(player):
        """
        валідація вводу корситувача, вибір персонажа можливий лише цифрами 1, 2 та 3
        """
        if not isinstance(player, int) or (player > 3):
            int(input("You can use only numbers 1, 2 or 3. Try again: "))
