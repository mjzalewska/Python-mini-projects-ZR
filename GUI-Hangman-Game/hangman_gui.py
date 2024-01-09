from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk


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

        # game screen
        self.game_screen_frm = tk.Frame(master=self, bg="black")
        self.game_screen_frm.pack(fill=tk.BOTH, expand=True)
        self.game_screen_frm.grid_rowconfigure(0, weight=1)
        self.game_screen_frm.grid_columnconfigure(0, weight=1)
        # gallows img
        self.gallows_orig_img = Image.open("Assets/gallows_0.png")
        resized = self.gallows_orig_img.resize((700, 180), Image.LANCZOS)
        self.gallows_img = ImageTk.PhotoImage(resized)
        # game screen label
        self.game_screen_lbl = tk.Label(master=self.game_screen_frm, bg="black", borderwidth=0, image=self.gallows_img)
        self.game_screen_lbl.pack(fill=tk.BOTH,expand=True)
        # secret word display frame
        self.secret_wrd_frm = tk.Frame(master=self, bg="black")
        self.secret_wrd_frm.pack(fill=tk.BOTH)
        self.secret_wrd_frm.grid_columnconfigure(0, weight=1)
        self.secret_wrd_frm.grid_rowconfigure(0, weight=1)
        # secret word display
        self.secret_wrd_lbl = tk.Label(master=self.secret_wrd_frm, bg="black", borderwidth=0,
                                       font=("Algerian", 15, "bold"), fg="white", width=15, pady=10, text="TEST")
        self.secret_wrd_lbl.pack()
        # letter entry frame
        self.letter_ent_frm = tk.Frame(master=self, bg="black")
        self.letter_ent_frm.pack(fill=tk.BOTH)
        self.letter_ent_frm.grid_columnconfigure(0, weight=1)
        self.letter_ent_frm.grid_columnconfigure(0, weight=1)
        # letter entry
        self.letter_ent = ttk.Entry(master=self.letter_ent_frm, width=16, background="black",
                                    font=("Algerian", 15, "bold"), justify=tk.CENTER)
        self.letter_ent.pack(ipady=6, pady=10)
        # submit button frame
        self.guess_btn_frm = tk.Frame(master=self, bg="black")
        self.guess_btn_frm.pack(fill=tk.X)
        self.guess_btn_frm.grid_columnconfigure(0, weight=1)
        self.guess_btn_frm.grid_rowconfigure(0, weight=1)
        # submit button
        self.guess_btn = ttk.Button(master=self.guess_btn_frm, text="TAKE A GUESS", padding=7)
        self.guess_btn.pack(pady=10)


if __name__ == '__main__':
    app = HangmanApp()
    app.mainloop()
