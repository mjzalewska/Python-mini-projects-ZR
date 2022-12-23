import csv
import random
import string


def print_header():
    print('_|    _|                                                                  ')
    print('_|    _|    _|_|_|  _|_|_|      _|_|_|  _|_|_|  _|_|      _|_|_|  _|_|_|_|')
    print('_|_|_|_|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|')
    print('_|    _|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|')
    print('_|    _|    _|_|_|  _|    _|    _|_|_|  _|    _|    _|    _|_|_|  _|    _|')
    print('                                    _|                                    ')
    print('                                 _|_|                                     ')


def greet():
    greeting = "Hello! Let's play hangman. Can you guess the secret word in 10 attempts?"
    print('*' * len(greeting))
    print(greeting)
    print('*' * len(greeting))


def import_wordlist(file_name):
    words = []
    with open(file_name, 'r') as f:
        data = csv.reader(f)
        for row in data:
            words.extend(row)
    return words


def choose_secret_word(word_list):
    secret_word = random.choice(word_list)
    return secret_word


def hide_word(word):
    hidden_word = ['*'] * len(word)
    print(f"The word I'm thinking of has {len(word)} letters: {''.join(hidden_word)}")
    return hidden_word


def find_index(word, char):
    return [idx for idx, letter in enumerate(word) if letter == char]


def unhide_word(matrix, indices, letter):
    for s_index in indices:
        matrix[s_index] = letter
    return matrix


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


def play():
    print_header()
    greet()

    word_bank = import_wordlist('wordlist.csv')
    secret_word = choose_secret_word(word_bank)
    hidden_secret = hide_word(secret_word)

    choices = ['y', 'n']
    missed_shots = 0
    game_on = True

    while game_on:
        print('Give me a letter in the range a-z: ')
        user_guess = input().casefold()
        letter_indexes = find_index(secret_word, user_guess)
        revealed_secret = ''.join(unhide_word(hidden_secret, letter_indexes, user_guess))

        if user_guess not in string.ascii_lowercase:
            print('Incorrect input!')
        else:
            if user_guess in secret_word:
                print(f'Correct! The secret word is now: {revealed_secret}')
                if '*' not in hidden_secret:
                    print('Congratulations! You\'ve unhidden all letters! You win!')
                    game_on = False
                else:
                    print("Would you like to take a shot at the whole word? Y/N")
                    choice_time = True
                    while choice_time:
                        user_choice = input().casefold()
                        if user_choice not in choices:
                            print("Incorrect input! Please choose Y or N!")
                        else:
                            if user_choice == 'y':
                                guess_all = input("Your guess: ").casefold()
                                if guess_all == secret_word:
                                    print("Correct! You win!")
                                    game_on = False
                                    choice_time = False
                                else:
                                    print("Sorry! You missed!")
                                    missed_shots += 1
                                    print()
                                    draw_hangman(missed_shots)
                                    print()
                                    choice_time = False
                            else:
                                print("No worries! Let's carry on!")
                                choice_time = False
            else:
                print('Sorry, you missed! Please try again!')
                missed_shots += 1
                print()
                draw_hangman(missed_shots)
                print()

        if missed_shots == 10:
            print('You missed 10 times! Game over')
            game_on = False


if __name__ == "__main__":
    play()
