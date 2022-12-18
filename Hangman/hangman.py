# wrong guess - dodaje element hangmana i rysuje od razu

# powinien tak długo pytać o litery aż albo się wypełnią wszystkie albo zgadanie słowo!!
# jak się wszystko wypełni to gra stop


import requests

api_url = 'https://api.api-ninjas.com/v1/randomword'
key = 'MFh/MWtikknsaXiJKQNa8Q==qLDPv9767gHid06X'
response = requests.get(api_url, params='noun', headers={'X-Api-Key': key})

secret_word = response.json()['word']
print(secret_word)

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


greeting = "Hello! Let's play hangman. Can you guess the secret word?"
print('*' * len(greeting))
print(greeting)
print('*' * len(greeting))

hidden_word = ['*'] * len(secret_word)
print(f"The word I'm thinking of has {len(secret_word)} letters: {''.join(hidden_word)}")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
game_on = True

while ''.join(hidden_word) != secret_word:
    print(f"Give me your letter: ")
    player_guess = input().casefold()
    if player_guess not in alphabet:
        print("Sorry, this is not a letter! Please try again!")
    else:
        if player_guess in secret_word:
            print("That's right!")
            print(f"The secret word is now: "
                  f"{''.join(unhide_word(hidden_word, find_index(secret_word, player_guess),player_guess))}")
            player_guess_all = input(f"Would you like to guess the whole word? Y/N: ")
            if player_guess_all.casefold()[0] == 'y':
                player_word = input("Your guess: ")
                if player_word == secret_word:
                    print("That's right! You win!")
                    break
                else:
                    print("Sorry, you missed! Please try again!")
            else:
                print("OK then. Let's carry on!")
        else:
            print("Sorry, you missed! Please try again!")


def draw_hangman():
    pass
