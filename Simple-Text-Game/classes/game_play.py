from file_manager import FileManager
from item import Item
from scene import Scene
from character import Hero, Enemy
from time import sleep


class GamePlay:
    game_state = 'initializing'
    hero = None
    enemy = None
    item = None
    current_scene = None
    available_commands = ['M', 'D', 'E', 'B', 'I', 'T', 'S', 'Q']

    @classmethod
    def show_welcome_screen(cls):
        print()
        print('You are now in the deserted castle undergrounds')
        print('Can you find your way out?')

    @classmethod
    def show_menu(cls):
        print('\n-----GAME MENU-----')
        if cls.current_scene.has_enemy():
            menu = FileManager().load_json_file(r'..\setup_files\game_menu.json')['enemies']
            for key, value in menu.items():
                print(f'{key} : {value}')
        else:
            menu = FileManager().load_json_file(r'..\setup_files\game_menu.json')['no_enemies']
            for key, value in menu.items():
                print(f'{key} : {value}')

    @classmethod
    def choose_character(cls):
        character_types = ['elf', 'mage', 'knight']
        print('\nChoose your character: Elf, Mage, Knight ')
        while True:
            character_choice = input('>>').casefold()
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
            if cls.current_scene.has_enemy():
                enemy_values = FileManager.load_json_file(r'..\setup_files\goblin.json')
                cls.enemy = Enemy(**enemy_values)
            else:
                cls.available_commands = ['M', 'D', 'B', 'I', 'T', 'S', 'Q']
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
                    match command:
                        case 'M':
                            cls.show_menu()
                        case 'D':
                            print(cls.current_scene)
                        case 'E':
                            cls.enemy.show_stats()
                        case 'B':
                            cls.hero.show_inventory()
                        case 'I':
                            print('Please type the name of the item whose stats you would like to see')
                            item_to_see = input().title()
                            item_values = FileManager.load_json_file(r'..\setup_files\items.json')[item_to_see]
                            cls.item = Item(**item_values)
                            cls.item.show_item_stats(item_to_see)
                        case 'T':
                            if cls.current_scene.items:
                                print('Which item would you like to take. Choose wisely. You can only take one!')
                                cls.current_scene.enumerate_items()
                                item_choice = input('>>').title()
                                item_values = FileManager.load_json_file(r'..\setup_files\items.json')[item_choice]
                                cls.item = Item(**item_values)
                                if item_choice in cls.current_scene.items:
                                    if item_choice.split()[1] == cls.hero.weapon: #nie można dodać itemów innych niż broń
                                        cls.hero.add_item(item_choice)
                                        cls.item.boost_char_stats(cls.hero)
                                    else:
                                        print('Are you sure you know how to use this? Better choose something else.')
                                else:
                                    print('No such item here!')
                            else:
                                print('Nothing interesting here...')
                        case 'S':
                            cls.hero.show_stats()
                        case 'Q':
                            print('Exiting the game...')
                            sleep(3)
                            break


GamePlay.play()
# add move_to_next_scene after item taken
# move directly to the next scene after item chosen
# import setup_files instead of path