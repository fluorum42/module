class GameOver(Exception):
    """
    В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.
    """
    def __init__(self, score, name):
        self.score = score
        self.name = name

class EnemyDown(Exception):
    """
    Функціонал не потрібен, тільки декларація.
    """
