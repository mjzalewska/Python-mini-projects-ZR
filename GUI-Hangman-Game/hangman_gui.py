import csv
import string
from random import choice
from time import sleep
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno


class HangmanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # root window
        self.title("The Hangman")
        self.color = self.configure(bg="black")
        self.geometry("700x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # container frame
        container = tk.Frame(master=self)
        container.grid(row=0, column=0, sticky="nswe")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # app buttons styling
        self.b_style = ttk.Style()
        self.b_style.configure("TButton", font=("Algerian", 15, "bold"), background="black",
                               width=15)
        self.b_style.map("TButton", background=[("active", "red")])

        # dictionary of child frame instances
        self.frames = {}
        for page in (TitlePage, GamePage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(TitlePage)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class TitlePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller

        # title frame
        self.header_frm = tk.Frame(master=self, bg="black")
        self.header_frm.pack(fill=tk.BOTH, expand=True)
        self.header_frm.grid_rowconfigure(0, weight=1)
        self.header_frm.grid_columnconfigure(0, weight=1)
        # title image
        self.original_img = Image.open("Assets/Hangman_red_font_black_bg.png")
        resized = self.original_img.resize((700, 360), Image.LANCZOS)
        self.title_img = ImageTk.PhotoImage(resized)
        self.title_lbl = tk.Label(master=self.header_frm, image=self.title_img, borderwidth=0)
        self.title_lbl.pack()
        # start button frame
        self.start_btn_frm = tk.Frame(master=self, bg="black")
        self.start_btn_frm.pack(fill=tk.X)
        self.start_btn_frm.grid_columnconfigure(0, weight=1)
        self.start_btn_frm.grid_rowconfigure(0, weight=1)
        # quit button frame
        self.quit_btn_frm = tk.Frame(master=self, bg="black")
        self.quit_btn_frm.pack(fill=tk.X)
        self.quit_btn_frm.grid_columnconfigure(0, weight=1)
        self.quit_btn_frm.grid_rowconfigure(0, weight=1)
        # buttons
        self.start_btn = ttk.Button(master=self.start_btn_frm, text="PLAY", padding=7,
                                    command=lambda: controller.show_frame(GamePage))
        self.start_btn.pack(pady=10)
        self.quit_btn = ttk.Button(master=self.quit_btn_frm, text="QUIT", padding=7, command=self.quit_game)
        self.quit_btn.pack(pady=10)

    @staticmethod
    def quit_game():
        exit()


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.game = GameLogic()

        # game screen
        self.game_screen_frm = tk.Frame(master=self, bg="black")
        self.game_screen_frm.pack(fill=tk.BOTH, expand=True)
        self.game_screen_frm.grid_rowconfigure(0, weight=1)
        self.game_screen_frm.grid_columnconfigure(0, weight=1)
        # game screen label
        self.game_screen_lbl = tk.Label(master=self.game_screen_frm, bg="black", borderwidth=0,
                                        image=self.game.update_gallows())
        self.game_screen_lbl.pack(fill=tk.BOTH, expand=True)
        # secret word display frame
        self.secret_wrd_frm = tk.Frame(master=self, bg="black")
        self.secret_wrd_frm.pack(fill=tk.BOTH)
        self.secret_wrd_frm.grid_columnconfigure(0, weight=1)
        self.secret_wrd_frm.grid_rowconfigure(0, weight=1)
        # secret word display
        self.secret_wrd_lbl = tk.Label(master=self.secret_wrd_frm, bg="black", borderwidth=0,
                                       font=("Algerian", 15, "bold"), fg="white", width=15, pady=10,
                                       text="".join(self.game.revealed_word))
        self.secret_wrd_lbl.pack()
        # letter entry frame
        self.letter_ent_frm = tk.Frame(master=self, bg="black")
        self.letter_ent_frm.pack(fill=tk.BOTH)
        self.letter_ent_frm.grid_columnconfigure(0, weight=1)
        self.letter_ent_frm.grid_columnconfigure(0, weight=1)
        # letter entry
        self.letter_ent = ttk.Entry(master=self.letter_ent_frm, width=16, background="black",
                                    font=("Algerian", 15, "bold"), justify=tk.CENTER)
        validate_cmd = (self.register(self.validate), "%P")
        invalid_cmd = (self.register(self.on_invalid, ))
        self.letter_ent.config(validate="focusout", validatecommand=validate_cmd, invalidcommand=invalid_cmd)
        self.letter_ent.pack(ipady=6, pady=10)
        # submit button frame
        self.guess_btn_frm = tk.Frame(master=self, bg="black")
        self.guess_btn_frm.pack(fill=tk.X)
        self.guess_btn_frm.grid_columnconfigure(0, weight=1)
        self.guess_btn_frm.grid_rowconfigure(0, weight=1)
        # submit button
        self.guess_btn = ttk.Button(master=self.guess_btn_frm, text="TAKE A GUESS", padding=7, command=self.run_game)
        self.guess_btn.pack(pady=10)
        # return button frame
        self.return_btn_frm = tk.Frame(master=self, bg="black")
        self.return_btn_frm.pack(fill=tk.X)
        self.return_btn_frm.grid_columnconfigure(0, weight=1)
        self.return_btn_frm.grid_rowconfigure(0, weight=1)
        # return button
        self.return_btn = ttk.Button(master=self.return_btn_frm, text="BACK", padding=7,
                                     command=self.go_back)
        self.return_btn.pack(pady=10)

    @staticmethod
    def validate(value):
        if len(value) == 1 and value in string.ascii_letters:
            return True
        else:
            return False

    def on_invalid(self):
        self.show_message("Incorrect input!", "red")

    def show_message(self, error="", color="black"):
        self.letter_ent.delete(0, tk.END)
        self.letter_ent.insert(0, error)
        self.letter_ent["foreground"] = color

    def go_back(self):
        self.controller.show_frame(TitlePage)
        self.reset()

    def reset(self):
        self.letter_ent.config(state="normal")
        self.guess_btn.config(state="normal")
        self.secret_wrd_lbl["text"] = ""
        self.letter_ent.delete(0,tk.END)
        self.game = GameLogic()

    def start_over(self):
        answer = askyesno(title='Play Again?',
                          message='Would you like to play again?')
        if answer:
            self.reset()

    def run_game(self):
        print(self.game.secret_word)
        player_guess = self.letter_ent.get().casefold()
        if len(player_guess) != 1:
            sleep(1)
            self.letter_ent.delete(0, tk.END)
            self.letter_ent["foreground"] = "black"
        else:
            if player_guess in self.game.secret_word:
                self.secret_wrd_lbl["text"] = self.game.show_word(player_guess)
            else:
                self.game.update_miss_count()
                self.game_screen_lbl["image"] = self.game.update_gallows()
            self.letter_ent.delete(0, tk.END)

        if self.game.is_winner() or self.game.is_game_over():
            self.game_screen_lbl["image"] = self.game.update_gallows()
            self.letter_ent.config(state="disabled")
            self.guess_btn.config(state="disabled")
            self.start_over()


class GameLogic:
    def __init__(self):
        self.word_list = self._import_wordlist("wordlist.csv")
        self.secret_word = self._choose_secret_word()
        self.revealed_word = len(self.secret_word) * ["*"]
        self.gallows_img = None
        self.misses = 0

    @staticmethod
    def _import_wordlist(file_name):
        words = []
        with open(file_name, "r") as f:
            data = csv.reader(f)
            for row in data:
                words.extend(row)
        return words

    def _choose_secret_word(self):
        return choice(self.word_list)

    def show_word(self, guess):
        for i, letter in enumerate(self.secret_word):
            if letter == guess:
                self.revealed_word[i] = letter
        return "".join(self.revealed_word)

    def update_miss_count(self):
        self.misses += 1

    def is_winner(self):
        if "*" not in self.revealed_word:
            return True
        else:
            return False

    def is_game_over(self):
        if self.misses == 8:
            return True
        else:
            return False

    def update_gallows(self):
        if self.is_winner():
            image_path = "Assets/gallows_winner.png"
        elif self.misses <= 8:
            image_path = f"Assets/gallows_{self.misses}.png"

        orig_img = Image.open(image_path)
        resized = orig_img.resize((700, 180))
        self.gallows_img = ImageTk.PhotoImage(resized)

        return self.gallows_img


if __name__ == '__main__':
    app = HangmanApp()
    app.mainloop()
