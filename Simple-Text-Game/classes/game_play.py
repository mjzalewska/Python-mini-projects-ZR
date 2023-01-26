import sys
from file_manager import FileManager
from item import Item
from scene import Scene
from character import Hero


class GamePlay:

    game_commands = ['H', 'D', 'I', 'T', 'Q']

    @classmethod
    def show_wellcome_screen(cls): # add greeting
        print('...')

    @classmethod
    def show_menu(cls):
        print('-----GAME MENU-----')
        menu_items = FileManager()
        menu = menu_items.load_json_file(r'..\setup_files\game_menu.json')[0]
        for key, value in menu.items():
            print(f'{key} : {value}')

    @classmethod
    def choose_character(cls):
        character_types = ['elf', 'mage', 'knight']
        print('Choose your character: Elf, Mage, Knight ')
        while True:
            character_choice = input().casefold()
            if character_choice in character_types:
                print(f'You have chosen: {character_choice.capitalize()}')
                return character_choice.capitalize()
            else:
                print('This is not a valid choice!')

    @classmethod
    def initialize_scene(cls):
        scene_values = FileManager.load_json_file(r'..\setup_files\scene1.json')
        current_scene = Scene(**scene_values)
        return current_scene

    @classmethod
    def initialize_hero(cls):
        character_values = FileManager.load_json_file(r'..\setup_files\{}'.format(cls.choose_character()))
        current_character = Hero(**character_values)
        return current_character

    @classmethod
    def play(cls):
        while True:
            print(f'Available commands: {"".join(cls.game_commands)}')
            command = input()
            if command not in cls.game_commands:
                print('Sorry I don\'t know this command. Please choose again!')
            else:
                match command:
                    case 'H':
                        cls.show_menu()
                    case 'D':
                        cls.initialize_scene().__str__()
                    case 'I':
                        cls.initialize_hero().show_inventory()
                    case 'T': #potencjalnie do usunięcia
                        pass
                    case 'Q':
                        break


        pass


