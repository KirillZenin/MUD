# MUD.py
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
        print('Type search to find something here')
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
            elif way == 'search':
                search(current_location)
        else:
            print('You already there!')
    return


def square():
    cls()
    print(
        '*____________________________*\n'
        '|   You are on the square    |\n'
        '*____________________________*\n'
        '\n A small village square with diverging streets in different directions and framed by low wooden houses'
    )


def inn():
    cls()
    print(
        '*____________________________*\n'
        '| You are in front of the inn|\n'
        '*____________________________*\n'
        '\n You are in front of the entrance to a small but cozy inn.'
    )


def road():
    cls()
    print(
        '*____________________________*\n'
        '|    You are on the road     |\n'
        '*____________________________*\n'
        '\n You see a long road going to the horizon, a clear field and nothing else'
    )


def mill():
    cls()
    print(
        '*____________________________*\n'
        '|      You are nearby mill   |\n'
        '*____________________________*\n'
        '\n'
    )


def forge():
    cls()
    print(
        '*____________________________*\n'
        '|    You are nearby forge    |\n'
        '*____________________________*\n'
        '\n'
    )


def search(current_location):
    print('\n*____________________________*')
    print('You are searching something here...')
    if current_location == 'square':
        print('You found a bunch of garbage here and nothing more.')
    elif current_location == 'inn':
        print('There is nothing useful here.')
    elif current_location == 'road':
        print('Only one broken wheel in the bushes.')
    elif current_location == 'mill':
        print('A few bags on the cart at the mill and thick and prickly bushes around. You do not want to go there.')
    elif current_location == 'forge':
        print('Here is a pile of scrap metal, but you don’t see anything useful for yourself.')
    else:
        print('Where are you man?? And how did you come there?')
    print('\n*____________________________*')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    start()
