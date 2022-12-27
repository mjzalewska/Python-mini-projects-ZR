# jeśli trzy zajęte obok siebie lub wszystkie zajęte, to koniec gry
# pytanie czy chce grać jeszcze raz - jak nie, kończymy


import random

# game_board = [''] * 9
game_board = ['X', 'X', '', 'X', '', 'X', 'X', 'X', '']


def greet():
    greeting = "Hello! Welcome to the tic-tac-toe game!"
    print("*" * len(greeting))
    print(greeting)
    print("*" * len(greeting))
    name = input("What's your name: \n")
    return name


def chose_game_mode():
    print("Please choose game mode: 1 - Player vs Player, 2 - Player vs Computer: ")
    while True:
        game_mode = input()
        if int(game_mode) in [1, 2]:
            return str(game_mode)
        else:
            print("Invalid input! Please choose 1 or 2")


def choose_sign():
    print("Player 1, please choose if you want to be \'X\' or \'O\':\n")
    while True:
        player_choice = input()
        if player_choice.casefold() not in ['x', 'o']:
            print("Sorry, invalid input! Please choose \'X\' or \'O\':\n")
        else:
            if player_choice.casefold() == 'x':
                print(f"Player 1, you have chosen \'X\'. Player 2 will play as  \'O\'")
                print("Let\'s start!")
                return player_choice
            else:
                print(f"Player 1, you have chosen \'O\'. Player 2 will play as  \'X\'")
                print("Let\'s start!")
                return player_choice


def choose_order(player_sign, player_name):
    order = random.choice(['X', 'O'])
    if order == player_sign:
        print(f"{player_name}, you will go fist")
        return order
    else:
        print("Player 2 will play first")
        return order


def draw_board(board):
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


def check_field(board, field_index):
    if not board[field_index]:
        return True
    else:
        return False


def comp_play(comp_sign, board):
    computer_choice = random.randint(0, 8)
    if check_field(board, computer_choice):
        board[computer_choice] = comp_sign
    else:
        comp_play(comp_sign, board)


def game(player_sign, board):
    game_on = True
    while game_on:
        print("Choose a field number from 1 to 9")
        player_choice = input()
        if not player_choice.isdigit() or 9 < int(player_choice) < 1:
            print("Sorry, this is not a valid choice. Choose a digit from 1 to 9")
        else:
            if board[int(player_choice) - 1]:
                print("Sorry, this field is already taken. Please choose another field number between 1 and 9.\n")
            else:
                board[int(player_choice) - 1] = player_sign
                game_on = False


def convert_to_bool(matrix):
    for item in matrix:
        if isinstance(item, list):
            return any([len(set(item)) == 1 for item in matrix])
        else:
            return len(set(matrix)) == 1


game_board = [
    'X', 'X', 'O',
    'X', 'X', 'X',
    'O', 'X', 'X'
]

h_fields = [game_board[index:index + 3] for index in range(0, len(game_board), 3)]
v_fields = [[item[i] for item in h_fields] for i in range(0, 3)]
l_cross_fields = [h_fields[i][i] for i in range(0, 3)]
r_cross_fields = [h_fields[i][2 - i] for i in range(0, 3)]


def check_winner():
    pass
# return winner's sign


