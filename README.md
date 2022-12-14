# module
module OOP
Створити інтерактивну гру в консолі, що базується на принципі "камень-ножиці-папір". Оцінка pylint - не менше 8

**Вимогу до проекту:**

1. Cтворити віртуальне оточення (python -m venv %env_name%).
2. Проект має бути в окремій директорії та в окремому репозиторії.
3. В проекті має бути файл .gitignore, всі файли які не мають версіюватись мають бути прописані там.
4. Master/Main branch має містити два порожніх файла: requirements.txt та scores.txt.
5. Розробка має вестись в гілці develop, яка утворена на базі master/main.
6. Завдання приймається виключно у виді pull-request з гілкі develop в master/main. 
7. **При невиконанні умов в пунктах 2-6 робота не буде розглядатись.**



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

**Структура проекта:**

1. В проекті мають бути файли requirements.txt та scores.txt для збереження додаткових бібіліотек і збереження рекордів гравців.
2. Файл settings.py має містити в собі всі константи (напр. кількість життів гравця)
3. Файл game_exceptions.py буде містити спеціальні винятки, які будуть контролювати ігровий процес.
4. В файлі models.py зберігати класи гравця та противника.
5. Файл game.py - основний файл, який запускається для гри.

**exceptions.py:**

- Містить клас GameOver - унаслідований від Exception. В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.
- Містить клас EnemyDown - унаслідований від Exception. Функціонал не потрібен, тільки декларація.

- **_Додаткове завдання:_**
    _Створити механізм збереження тільки топ 10 рекордів._

**models.py - class Enemy:**

- Атрибути класу - level, lives.
- Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.

- Містить два методи:
  - статичний select_attack(): повертає випадкове число від 1 до 3.
  - decrease_lives(self): зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown.
  
**models.py - class Player:**

- Атрибути: name, lives, score, allowed_attacks.
- Конструктор приймає ім'я гравця. 
  - Кількість життів отримується з settings. 
  - Рахунок дорівнює нулю.

- Методи: 
  - статичний fight(attack, defense) - повертає результат атаки/захисту:
    - 0 нічия
    - -1 aтака/захист невдалі.
    - 1 атака/захист вдалі.

  - decrease_lives(self) - те саме, що і Enemy.decrease_lives(), викликає виняток GameOver.

  - attack(self, enemy_obj) 
    - отримує input (1, 2, 3) від користувача;
    - обирає атаку противника з об'екту enemy_obj; 
    - викликає метод fight(); 
    - Якщо результат 0 - вивести "It's a draw!"
    - Якщо 1 = "You attacked successfully!" та зменшує кількість життів противника на 1;
    - Якщо -1 = "You missed!"

  - defence(self, enemy_obj) - такий самий, як метод attack(), тільки в метод fight першим передається атака противника, та при вдалій атаці противника викликається метод decrease_lives гравця.

**game.py:**

- Містить блок на перевірку імені модуля (main)
- В середині if блок try/except. 
- try запускає функцію play()
- except обробляє два винятки: 
  - GameOver - виводить на екран повідомлення про завершення гри, записує результат в таблицю рекордів. 
  - KeyboardInterrupt - pass. 
- finally виводить на екран "Good bye!"

**game.py - play():**

- Гравець вводить ім'я
- Створюється об'єкт player
- level = 1
- Створюється об'єкт enemy.
- В бескінечному циклі викликаються методи attack та defence об'єкту player
- при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем

**Додаткові завдання (обов'язкові):**
1. Додати валідацію вводу корситувача.
2. Розширити ігрове меню:
   1. Додати команду show scores - яка виводить записи із файлу scores.txt
   2. Додати команду exit - викликає виняток та завершує роботу програми.
   3. Додати команду help - виводить список можливих команд (зберігати в файлі налаштувань).

**Додаткове завдання (необов'язкове)** 
1. Перед початком гри запропонувати режими гри: Normal або Hard
2. При виборі Hard кілкість життів противника множиться на N та кількість очків множиться на N
   1. N зберігається в налаштуваннях 
3. Додати в запис рекордів режим гри (Hard/Normal)


    наприклад, якщо hard_mode_multiplier = 3, то на першому рівні противник має 3 життя,
    за успішну атаку гравець отримує 3 очка, за перемогу над противником отримує 15 балів 
