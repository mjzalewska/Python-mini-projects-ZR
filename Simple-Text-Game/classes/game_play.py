from file_manager import FileManager
from item import Item
from scene import Scene
from character import Hero
from time import sleep


class GamePlay:
    game_state = 'initializing'
    hero = None
    current_scene = None
    available_commands = ['M', 'D', 'I', 'T', 'Q']

    @classmethod
    def show_welcome_screen(cls):
        print()
        print('You are now in the deserted castle undergrounds')
        print('Can you find your way out?')

    @classmethod
    def show_menu(cls):
        print('\n-----GAME MENU-----')
        menu_items = FileManager()
        menu = menu_items.load_json_file(r'..\setup_files\game_menu.json')[0]
        for key, value in menu.items():
            print(f'{key} : {value}')

    @classmethod
    def choose_character(cls):
        character_types = ['elf', 'mage', 'knight']
        print('\nChoose your character: Elf, Mage, Knight ')
        while True:
            character_choice = input().casefold()
            if character_choice in character_types:
                print(f'You have chosen: {character_choice.capitalize()}\n')
                return character_choice
            else:
                print('This is not a valid choice!')

    @classmethod
    def initialize(cls):
        if FileManager.is_scene_available(r'..\setup_files\scene1.json'):
            cls.show_welcome_screen()
            scene_values = FileManager.load_json_file(r'..\setup_files\scene1.json')
            cls.current_scene = Scene(**scene_values)
            hero_values = FileManager.load_json_file(r'..\setup_files\{}.json'.format(cls.choose_character()))
            cls.hero = Hero(**hero_values)
            cls.current_scene.show_intro()
            cls.show_menu()

            cls.game_state = 'playing'
        else:
            if not cls.current_scene.next_scene():
                print('Congratulations, you have finished the game!')
                print('Do you want to play again?Y/N')
                replay = input()
                if replay[0].casefold() == 'y':
                    cls.play()
                else:
                    exit()

    @classmethod
    def play(cls):
        while True:
            if cls.game_state == 'initializing':
                cls.initialize()
            else:
                print(f'\nAvailable commands: {",".join(cls.available_commands)}\n')
                command = input('>> ').capitalize()
                if command not in cls.available_commands:
                    print('Sorry I don\'t know this command. Please choose again!')
                else:
                    match command: # add show hero stats and show enemy stats
                        case 'M':
                            cls.show_menu()
                        case 'D':
                            print(cls.current_scene)
                        case 'I':
                            cls.hero.show_inventory()
                        case 'T':
                            if cls.current_scene.items:
                                print('Which item would you like to take. You can only take one!')
                                cls.current_scene.enumerate_items(cls.hero)
                                item_choice = input().title()
                                if item_choice in cls.current_scene.items:
                                    cls.hero.add_item(item_choice)
                                    cls.current_scene.remove_item(item_choice)
                                    # when item taken should boost stats
                                else:
                                    print('No such item here!')
                            else:
                                print('Nothing interesting here...')
                        case 'Q':
                            print('Exiting the game...')
                            sleep(3)
                            break


GamePlay.play()
