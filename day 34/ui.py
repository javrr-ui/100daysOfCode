from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0")
        self.score_label.grid(column=1, row=0)

        self.window.mainloop()
