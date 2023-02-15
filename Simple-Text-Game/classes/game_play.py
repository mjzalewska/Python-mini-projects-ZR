from file_manager import FileManager
from item import Item
from scene import Scene
from character import Hero, Enemy
from time import sleep


class GamePlay:
    scene_number = 1
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
            menu = FileManager().load_json_file(r'..\json_files\game_menu.json')['enemies']
            for key, value in menu.items():
                print(f'{key} : {value}')
        else:
            menu = FileManager().load_json_file(r'..\json_files\game_menu.json')['no_enemies']
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
        if FileManager.is_scene_available(rf'..\json_files\scene{cls.scene_number}.json'):
            # cls.show_welcome_screen()
            scene_values = FileManager.load_json_file(fr'..\json_files\scene{cls.scene_number}.json')
            cls.current_scene = Scene(**scene_values)
            if cls.current_scene.has_enemy():
                enemy_values = FileManager.load_json_file(r'..\json_files\goblin.json')
                cls.enemy = Enemy(**enemy_values)
            else:
                cls.available_commands = ['M', 'D', 'B', 'I', 'T', 'S', 'Q']
            # hero_values = FileManager.load_json_file(r'..\json_files\{}.json'.format(cls.choose_character()))
            # cls.hero = Hero(**hero_values)
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
    def sort_game_items(cls, **kwargs):
        collectibles = {'Other collectibles': [], 'Weapons': []}

        for key, value in kwargs.items():
            if value['collectible']:
                if value['type'] in ['Other']:
                    collectibles['Other collectibles'].append(key)
                elif value['type'] in ['Weapon']:
                    collectibles['Weapons'].append(key)
        return collectibles

    @classmethod
    def collect_items(cls):
        if cls.current_scene.items:
            print('Which item would you like to take. Choose wisely. You can only take one!')
            cls.current_scene.enumerate_items()
            item_choice = input('>>').title()
            items = FileManager.load_json_file(r'..\json_files\items.json')
            item_values = items[item_choice]
            cls.item = Item(**item_values)
            collectibles = cls.sort_game_items(**items)
            if item_choice in cls.current_scene.items:
                if item_choice.split()[1] == cls.hero.weapon or \
                        item_choice in collectibles['Other collectibles']:
                    cls.hero.add_item(item_choice)
                    cls.item.boost_char_stats(cls.hero)
                else:
                    print('You cannot take that. Better choose something else.')
            else:
                print('No such item here!')
        else:
            print('Nothing interesting here...')

    @classmethod
    def load_next(cls):
        if cls.current_scene.next_scene:
            cls.game_state = 'initializing'
            cls.scene_number = cls.current_scene.next_scene
            cls.initialize()

    @classmethod
    def play(cls):
        cls.show_welcome_screen()
        hero_values = FileManager.load_json_file(r'..\json_files\{}.json'.format(cls.choose_character()))
        cls.hero = Hero(**hero_values)
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
                            item_values = FileManager.load_json_file(r'..\json_files\items.json')[item_to_see]
                            cls.item = Item(**item_values)
                            cls.item.show_item_stats(item_to_see)
                        case 'T':
                            cls.collect_items()
                            cls.load_next()
                        case 'S':
                            cls.hero.show_stats()
                        case 'Q':
                            print('Exiting the game...')
                            sleep(3)
                            break


GamePlay.play()
# when choosing item to take - if something else is typed instead, error is thrown (add error handling)