"""
Кількість життів для класa Player
"""
LIVES = 5


def do_work():
    """ Function to handle command line usage"""
    commands = ['help', 'show score', 'exit']
    if len(commands) == 0:
        print('You have not passed any commands in!')
    else:
        for command_input in commands:
            if command_input == 'help':
                print('Basic command line program')
                print('Options:')
                print('help -> Show this basic help menu.')
                print('score -> Show a score')
                print('exit -> Exit the game.')
                print('start -> Start the game.')

def show_score():
    with open('scores.txt', 'r', encoding="utf8") as file:
        print(file.read())
