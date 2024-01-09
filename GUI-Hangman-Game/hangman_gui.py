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
            frame.grid(row=0, column=0, sticky="nswe")

        self.show_frame(TitlePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class TitlePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()

        # title frame
        self.header_frm = tk.Frame(master=self, bg="black")
        self.header_frm.pack(fill=tk.BOTH, expand=True)
        self.header_frm.grid_rowconfigure(0, weight=1)
        self.header_frm.grid_columnconfigure(0, weight=1)
        # title image
        self.original_img = Image.open(
            "C:\\Users\\mjarz\\PycharmProjects\\Python-mini-projects-Z2J\\GUI-Hangman-Game\\Hangman_red_font_black_bg.png")
        resized = self.original_img.resize((700, 360), Image.LANCZOS)
        self.title_img = ImageTk.PhotoImage(resized)
        self.title_lbl = tk.Label(master=self, image=self.title_img, borderwidth=0)
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

        # game screen
        self.game_screen_frm = tk.Frame(master=self, bg="black")
        self.game_screen_frm.pack(fill=tk.BOTH, expand=True)
        self.game_screen_frm.grid_rowconfigure(0, weight=1)
        self.game_screen_frm.grid_columnconfigure(0, weight=1)
        # secret word frame
        self.secret_wrd_frm = tk.Frame(master=self, bg="black")
        self.secret_wrd_frm.pack(fill=tk.X)
        self.secret_wrd_frm.grid_columnconfigure(0, weight=1)
        self.secret_wrd_frm.grid_rowconfigure(0, weight=1)
        # guess button frame
        self.guess_btn_frm = tk.Frame(master=self, bg="black")
        self.guess_btn_frm.pack(fill=tk.X)
        self.guess_btn_frm.grid_columnconfigure(0, weight=1)
        self.guess_btn_frm.grid_rowconfigure(0, weight=1)
        # submit button
        self.submit_btn = ttk.Button(master=self, text="TAKE A GUESS", padding=7)


if __name__ == '__main__':
    app = HangmanApp()
    app.mainloop()
