# gracz wybiera swój znak - done
# losujemy kto zaczyna (x czy o i odpowiednio pytanie o pole) - done
# komputer losuje pole - done
# pytamy gracza o pole - done

# jeśli pole zajęte, to info, że tutaj nie można postawić
# j.w. - komputer

# sprawdzamy czy 3 pola obok siebie zajęte
# jeśli trzy zajęte obok siebie lub wszystkie zajęte, to koniec gry
# pytanie czy chce grać jeszcze raz - jak nie, kończymy


import random

print('*' * 38)
print("Hello! Welcome to the tic-tac-toe game!")
print('*' * 38)
print('\n')

name = input("Please, state your name (no swearwords, please ;-)\n")


def choose_sign():
    print("Please choose if you want to be \'X\' or \'O\':\n")
    while True:
        player_choice = input()
        if player_choice.casefold() not in ['x', 'o']:
            print("Sorry, this is not a valid choice. Please choose \'X\' or \'O\':\n")
        else:
            if player_choice.casefold() == 'x':
                print(f"You have chosen \'X\'. I will be \'O\'")
                print("Let\'s start!")
                return player_choice
            else:
                print(f"You have chosen \'O\'. I will be \'X\'")
                print("Let\'s start!")
                return player_choice


def choose_order(player, player_name):
    order = random.choice(['X', 'O'])
    if order == player:
        print(f"{player_name} you will go fist")
        return order
    else:
        print("Computer will play first")
        return order


def draw_board(board): # tutaj funkcja game

    print('|'.center(17) + '|'.center(3))
    print(f" {board[0]}".center(8) + '|' + f"{board[1]}".center(9) + '|' + f" {board[2]}".center(8))
    print('|'.center(17) + '|'.center(3))
    print('---------' * 3)
    print('|'.center(17) + '|'.center(3))
    print(f" {board[3]}".center(8) + '|' + f"{board[4]}".center(9) + '|' + f" {board[5]}".center(8))
    print('|'.center(17) + '|'.center(3))
    print('---------' * 3)
    print('|'.center(17) + '|'.center(3))
    print(f" {board[6]}".center(8) + '|' + f"{board[7]}".center(9) + '|' + f" {board[8]}".center(8))
    print('|'.center(17) + '|'.center(3))

def comp_play():# dodać do matrycy (najpierw check czy można)
    computer_choice = random.randint(0, 8)
    if computer_choice:
        pass # check czy pole zajęte-jak nie, to dodać do matrycy

    return computer_choice

def game(): #dodać argumenty
    game_on = True
    while game_on:
        print("Choose a field number from 1 to 9")
        player_choice = input()
        if not player_choice.isdigit() or 9 < int(player_choice) < 1:
            print("Sorry, this is not a valid choice. Choose a digit from 1 to 9")
        else:
             # tutaj dodajemy wybór gracza do matrycy


def check_board(computer_choice, player_choice): # check czy pole zajęte
    board = [''] * 9



def check_result():
    pass