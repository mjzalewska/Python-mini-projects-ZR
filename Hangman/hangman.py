# powinien tak długo pytać o litery aż albo się wypełnią wszystkie
# jak się wszystko wypełni to gra stop
# podzielić logikę na mniejsze funkcje + wpleść funchę draw_hangman
# dodać "would you like to play again? "
import random
import word_list

secret_word = random.choice(word_list.words)
print(secret_word) # do wywalenia na końcu

print("""

 _|    _|
 _|    _|    _|_|_|  _|_|_|      _|_|_|  _|_|_|  _|_|      _|_|_|  _|_|_|
 _|_|_|_|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|
 _|    _|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|
 _|    _|    _|_|_|  _|    _|    _|_|_|  _|    _|    _|    _|_|_|  _|    _|
                                     _|
                                 _|_|
""")


# helper functions
def find_index(word, char):
    return [idx for idx, letter in enumerate(word) if letter == char]


def unhide_word(matrix, indices, letter):
    for s_index in indices:
        matrix[s_index] = letter
    return matrix


greeting = "Hello! Let's play hangman. Can you guess the secret word in 11 moves?"
print('*' * len(greeting))
print(greeting)
print('*' * len(greeting))

hidden_word = ['*'] * len(secret_word)
print(f"The word I'm thinking of has {len(secret_word)} letters: {''.join(hidden_word)}")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
game_on = True
missed_shots = 0

while ''.join(hidden_word) != secret_word:
    print(f"Give me your best guess: ")
    player_guess = input().casefold()
    if player_guess not in alphabet:
        print("Sorry, this is not a letter! Please try again!")
    else:
        if player_guess in secret_word:
            print("That's right!")
            print(f"The secret word is now: "
                  f"{''.join(unhide_word(hidden_word, find_index(secret_word, player_guess),player_guess))}")
            player_guess_all = input(f"Would you like to take a shot at the whole word? Y/N: ")
            if player_guess_all.casefold()[0] == 'y':
                player_word = input("Your guess: ")
                if player_word == secret_word:
                    print("That's right! You win!")
                    break
                else:
                    print("Sorry, you missed! Please try again!")
                    missed_shots += 1
            else:
                print("OK then. Let's carry on!")
        else:
            print("Sorry, you missed! Please try again!")
            missed_shots += 1


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
