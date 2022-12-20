import csv
import os
import random


def print_header():
    print("""
    * ********************************************************************************
    * ****************************************************************************** *
    * * _|    _|                                                                   * *  
    * * _|    _|    _|_|_|  _|_|_|      _|_|_|  _|_|_|  _|_|      _|_|_|  _|_|_|   * *   
    * * _|_|_|_|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _| * *
    * * _|    _|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _| * *
    * * _|    _|    _|_|_|  _|    _|    _|_|_|  _|    _|    _|    _|_|_|  _|    _| * *
    * *                                     _|                                     * *
    * *                                   _|_|                                     * *
    * ****************************************************************************** *
    **********************************************************************************
    """)


def greet():
    greeting = "Hello! Let's play hangman. Can you guess the secret word in 10 attempts?"
    print('*' * len(greeting))
    print(greeting)
    print('*' * len(greeting))


def clear_screen():
    """
    Helper function to clear terminal
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def import_wordlist(file_name):
    words = []
    with open(file_name, 'r') as f:
        data = csv.reader(f)
        for row in data:
            words.extend(row)
    return words


def choose_secret_word(word_list):
    secret_word = random.choice(word_list)
    print(secret_word)  # do wywalenia na końcu
    return secret_word


def hide_word(word):  # secret word
    hidden_word = ['*'] * len(word)
    print(f"The word I'm thinking of has {len(word)} letters: {''.join(hidden_word)}")
    return hidden_word


def find_index(word, char):
    return [idx for idx, letter in enumerate(word) if letter == char]


def unhide_word(matrix, indices, letter):
    for s_index in indices:
        matrix[s_index] = letter
    return matrix


def take_and_check_input(prompt, warning, criteria=None):
    while True:
        user_reply = input(prompt).casefold()
        if user_reply in criteria:
            return user_reply
        else:
            return warning


def check_result(user_input, secret_word):
    if user_input in secret_word or user_input == secret_word:
        return True
    else:
        return False


def print_screen(): #decide if needed
    pass


def draw_hangman(counter):
    if counter == 1:
        print("___________")
    elif counter == 2:
        print("___________")
        print("|")
        print("|")
    elif counter == 3:
        print("___________")
        print("|")
        print("|")
        print("|")
        print("|")
    elif counter == 4:
        print("___________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif counter == 5:
        print("___________")
        print("|      ( )")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif counter == 6:
        print("___________")
        print("|      ( )")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
    elif counter == 7:
        print("___________")
        print("|      ( )")
        print("|      /|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif counter == 8:
        print("___________")
        print("|      ( )")
        print("|      /|\\")
        print("|")
        print("|")
        print("|")
        print("|")
    elif counter == 9:
        print("___________")
        print("|      ( )")
        print("|      /|\\")
        print("|      / ")
        print("|")
        print("|")
        print("|")
    elif counter == 10:
        print("___________")
        print("|      ( )")
        print("|      /|\\")
        print("|      / \\")
        print("|")
        print("|")
        print("|")


def run():
    word_bank = import_wordlist('wordlist.csv')
    secret_word = choose_secret_word(word_bank)
    hidden_secret = hide_word(secret_word)
    game_on = True
    missed_shots = 0

    print_header()
    greet()
    while game_on:
        pass




# OLD - to be deleted
# def take_a_guess(wrd_list, word):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     yes_no = ['y', 'n']
#     missed_shots = 0
#
#     while missed_shots < 10:
#         player_guess = input(f"Give me your best shot: ").casefold()
#         if player_guess not in alphabet:
#             print("Sorry, this is not a letter! Please name a letter in range a-z!")
#
#         elif player_guess in hide_word(word):
#             print("You have already used that letter! Please name another one!")
#
#         elif player_guess in choose_secret_word(wrd_list):
#             print("That's right!")
#             print(f"The secret word is now: "
#                   f"{''.join(unhide_word(hide_word(word), find_index(choose_secret_word(wrd_list), player_guess), player_guess))}")
#             if '*' not in hide_word(word):
#                 print("You've unhidden the word! You win!")
#                 break
#             # else:
#             #     print(f"Would you like to take a shot at the whole word? Y/N: ")  # tutaj jest problem
#             #     while True:
#             #         guess_all = input()
#             #         if guess_all.casefold()[0] not in ['y', 'n']:
#             #             print("Sorry, I didn't understand that. Please answer Y/N")
#             #         elif guess_all.casefold()[0] in ['y', 'n']:
#             #             if guess_all.casefold()[0] == 'y':
#             #                 player_word = input("Your guess: ")
#             #                 if player_word == secret_word:
#             #                     print("That's right! You win!")
#             #                     break
#             #                 else:
#             #                     print("Sorry, you missed! Please try again!")
#             #                     missed_shots += 1
#             #             else:
#             #                 print("OK. Let's carry on then!")
#
#         else:
#             # if player_guess not in choose_secret_word(wrd_list):
#             print("Sorry, you missed! Please try again!")
#             missed_shots += 1
#             if missed_shots >= 10:
#                 print("You missed 10 times! Game over!")
#
