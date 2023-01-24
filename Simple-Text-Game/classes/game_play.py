# a method for using items?
from file_manager import FileManager


class GamePlay:



    @classmethod
    def show_menu(cls):
        print("-----GAME MENU-----")
        menu_items = FileManager()
        menu = menu_items.load_json_file(r'..\setup_files\game_menu.json')[0]
        for key, value in menu.items():
            print(f"{key} : {value}")

    @classmethod
    def choose_character(cls):


    @classmethod
    def make_choice(cls):
        pass

    @classmethod
    def play(cls):
        pass

    @classmethod
    def finish(cls):
        pass



