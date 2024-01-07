from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, Button, Frame, Label


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # root window
        self.title("The Hangman")
        self.color = self.configure(bg="black")
        self.geometry("700x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # buttons style
        self.b_style = ttk.Style()
        self.b_style.configure("TButton", font=("Algerian", 15, "bold"), foreground="#910c20", background="black",
                               width=15)
        self.b_style.map("TButton", background=[("active", "red")])
        # frames
        self.main_frm = Frame(master=self)
        self.main_frm.grid(row=0, column=0, sticky="nswe")
        self.header_frm = Frame(master=self.main_frm, bg="black")
        self.header_frm.pack(fill=tk.BOTH, expand=True)
        self.header_frm.grid_rowconfigure(0, weight=1)
        self.header_frm.grid_columnconfigure(0, weight=1)

        self.start_btn_frm = Frame(master=self.main_frm, bg="black")
        self.start_btn_frm.pack(fill=tk.X)
        self.start_btn_frm.grid_columnconfigure(0, weight=1)
        self.start_btn_frm.grid_rowconfigure(0, weight=1)

        self.quit_btn_frm = Frame(master=self.main_frm, bg="black")
        self.quit_btn_frm.pack(fill=tk.X)
        self.quit_btn_frm.grid_columnconfigure(0, weight=1)
        self.quit_btn_frm.grid_rowconfigure(0, weight=1)

        # buttons
        self.start_btn = ttk.Button(master=self.start_btn_frm, text="PLAY", padding=7)
        self.start_btn.grid(row=0, column=0, pady=10)
        self.quit_btn = ttk.Button(master=self.quit_btn_frm, text="QUIT", padding=7, command=self.quit_game)
        self.quit_btn.grid(row=0, column=0, pady=10)

        # title image
        self.original_img = Image.open("Hangman_red_font_black_bg.png")
        resized = self.original_img.resize((650, 360), Image.LANCZOS)
        self.title_img = ImageTk.PhotoImage(resized)
        self.title_lbl = Label(master=self.header_frm, image=self.title_img, borderwidth=0)
        self.title_lbl.grid(row=0, column=0)


    @staticmethod
    def quit_game():
        exit()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
