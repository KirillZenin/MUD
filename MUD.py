# MUD.py авторы Кострулев и Зенин
import os


def start():
    cls()
    print(
        '*__________________________________*\n'
        '|  Mini MUD game for one player    |\n'
        '*__________________________________*\n'
        '\n'
        '\n'
    )
    option = ''
    options = {'start': True, 'exit': False}
    while option not in options:
        print('Choose: {}/{}'.format(*options))
        option = input()
    if options[option]:
        cls()
        square()
        way = ''
    current_location = 'square'
    locations = {'square', 'forge', 'mill', 'inn', 'road'}
    while way != 'quit':
        print('Choose: {}/{}/{}/{}/{}'.format(*locations))
        print('\nType "quit" to finish game')
        way = input()
        if current_location != way:
            if way == 'road':
                current_location = 'road'
                road()
            elif way == 'inn':
                current_location = 'inn'
                inn()
            elif way == 'square':
                current_location = 'square'
                square()
            elif way == 'mill':
                current_location = 'mill'
                mill()
            elif way == 'forge':
                current_location = 'forge'
                forge()
        else:
            print('You already there!')
    return


def square():
    cls()
    print(
        '*____________________________*\n'
        '|   You are on the square    |\n'
        '*____________________________*\n'
    )


def inn():
    cls()
    print(
        '*____________________________*\n'
        '| You are in front of the inn|\n'
        '*____________________________*\n'
    )


def road():
    cls()
    print(
        '*____________________________*\n'
        '|    You are on the road     |\n'
        '*____________________________*\n'
    )


def mill():
    cls()
    print(
        '*____________________________*\n'
        '|      You are nearby mill   |\n'
        '*____________________________*\n'
    )


def forge():
    cls()
    print(
        '*____________________________*\n'
        '|    You are nearby forge    |\n'
        '*____________________________*\n'
    )


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    start()
