from .file_manager import FileManager
from .item import Item
from .scene import Scene
from .character import Hero, Enemy
from time import sleep


class GamePlay:
    scene_number = 1
    game_state = 'initializing'
    hero = None
    enemy = None
    item = None
    target_item = None
    current_scene = None
    available_commands = None

    @classmethod
    def show_welcome_screen(cls):
        print()
        print('You are now in the deserted castle undergrounds')
        print('Can you find your way out?')

    @classmethod
    def show_menu(cls):
        print('\n-----GAME MENU-----')
        if cls.current_scene.has_enemy():
            menu = FileManager().load_json_file(r'.\json_files\game_menu.json')['enemies']
            for key, value in menu.items():
                print(f'{key} : {value}')
        else:
            menu = FileManager().load_json_file(r'.\json_files\game_menu.json')['no_enemies']
            for key, value in menu.items():
                print(f'{key} : {value}')

    @classmethod
    def choose_character(cls):
        character_types = ['elf', 'mage', 'knight']
        print('\nChoose your character: Elf, Mage, Knight ')
        while True:
            character_choice = input('>> ').casefold()
            if character_choice in character_types:
                print(f'You have chosen: {character_choice.capitalize()}\n')
                return character_choice
            else:
                print('This is not a valid choice!')

    @classmethod
    def initialize(cls):
        if FileManager.is_scene_available(rf'.\json_files\scene{cls.scene_number}.json'):
            scene_values = FileManager.load_json_file(fr'.\json_files\scene{cls.scene_number}.json')
            cls.current_scene = Scene(**scene_values)
            if cls.current_scene.has_enemy():
                enemy_values = FileManager.load_json_file(r'.\json_files\goblin.json')
                cls.enemy = Enemy(**enemy_values)
                cls.available_commands = ['M', 'D', 'B', 'S', 'E', 'F', 'R', 'I', 'T', 'L', 'U', 'Q']
            else:
                cls.available_commands = ['M', 'D', 'B', 'S', 'I', 'T', 'L', 'U', 'Q']
            cls.current_scene.show_intro()
            cls.show_menu()

            cls.game_state = 'playing'

    @classmethod
    def sort_game_items(cls, **kwargs):
        collectibles = {'Weapons': [], 'Other collectibles': [], 'Non-collectibles': []}

        for key, value in kwargs.items():
            if value['collectible']:
                if value['type'] in ['Other']:
                    collectibles['Other collectibles'].append(key)
                elif value['type'] in ['Weapon']:
                    collectibles['Weapons'].append(key)
            else:
                collectibles['Non-collectibles'].append(key)
        return collectibles

    @classmethod
    def collect_items(cls):
        while True:
            if cls.current_scene.items:
                items = FileManager.load_json_file(r'.\json_files\items.json')
                collectibles = cls.sort_game_items(**items)
                if all([True if item in collectibles['Non-collectibles'] else False for item in
                        cls.current_scene.items]):
                    print("Nothing interesting here...")
                    break
                else:
                    print('Which item would you like to take. Choose wisely. You can only take one!')
                    cls.current_scene.enumerate_items()
                    item_choice = input('>> ').title()
                    if item_choice in cls.current_scene.items:
                        item_values = items[item_choice]
                        cls.item = Item(**item_values)
                        if item_choice.split()[1] == cls.hero.weapon or \
                                item_choice in collectibles['Other collectibles']:
                            cls.hero.add_item(item_choice)
                            cls.item.boost_char_stats(cls.hero)
                            return True
                        else:
                            print('\nYou cannot take that. Better choose something else.')
                    else:
                        print('No such item here!Try again.')
                        continue
            else:
                print('Nothing interesting here...')
                return True

    @classmethod
    def use_items(cls):
        print("Your inventory:")
        cls.hero.show_inventory()
        print("Which item would you like to use?")
        while True:
            item_to_use = input('>> ').title()
            if item_to_use not in cls.hero.inventory:
                print('Sorry there\'s nothing like that in your backpack!')
            else:
                print(f'Which item would you like to use {item_to_use} on?\n')
                print('Your options: ')
                cls.current_scene.enumerate_items()
                target_item = input('>> ').title()
                if target_item in cls.current_scene.items:
                    item_values = FileManager.load_json_file(r'.\json_files\items.json')[target_item]
                    cls.target_item = Item(**item_values)
                    if item_to_use == cls.target_item.complementary_item:
                        print(f'You\'ve used {item_to_use} on {target_item}. It worked!')
                        print(f'{cls.target_item.action_result}')
                        break
                    else:
                        print('This will not work. Try something else.')
                else:
                    print('There\'s nothing like that here!')
                    break

    @classmethod
    def leave_items(cls):
        if len(cls.hero.inventory) > 0:
            print('Type the name of the item you\'d like to remove from your backpack')
            while True:
                item_to_remove = input('>> ').title()
                if item_to_remove in cls.hero.inventory:
                    item_values = FileManager.load_json_file(r'.\json_files\items.json')[item_to_remove]
                    cls.item = Item(**item_values)
                    cls.hero.remove_item(item_to_remove)
                    cls.item.reduce_char_stats(cls.hero)
                    break
                else:
                    print('There is no such item in your backpack')
        else:
            print('Your backpack is empty!')

    @classmethod
    def load_next(cls):
        if cls.current_scene.next_scene:
            cls.game_state = 'initializing'
            cls.scene_number = cls.current_scene.next_scene
            print("\nLoading next scene...\n")
            sleep(3)
            cls.initialize()
        else:
            print('Congratulations, you have finished the game!')
            print('Do you want to play again?Y/N')
            replay = input()
            if replay[0].casefold() == 'y':
                cls.scene_number = 1
                cls.game_state = 'initializing'
                cls.play()
            else:
                exit()

    @classmethod
    def play(cls):
        cls.show_welcome_screen()
        hero_values = FileManager.load_json_file(rf'.\json_files\{cls.choose_character()}.json')
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
                        case 'F':
                            if cls.hero.fight_enemy(cls.enemy):
                                cls.load_next()
                            else:
                                exit()
                        case 'R':
                            if cls.hero.run_from_enemy():
                                cls.load_next()
                            else:
                                exit()
                        case 'B':
                            cls.hero.show_inventory()
                        case 'I':
                            print('Please type the name of the item whose stats you would like to see')
                            item_to_see = input().title()
                            item_values = FileManager.load_json_file(r'.\json_files\items.json')[item_to_see]
                            cls.item = Item(**item_values)
                            cls.item.show_item_stats(item_to_see)
                        case 'T':
                            if cls.collect_items():
                                cls.load_next()
                            else:
                                continue
                        case 'S':
                            cls.hero.show_stats()
                        case 'L':
                            cls.leave_items()
                        case 'U':
                            cls.use_items()
                            cls.load_next()
                        case 'Q':
                            print('Exiting the game...')
                            sleep(3)
                            exit()
