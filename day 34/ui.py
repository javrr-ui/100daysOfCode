from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250)
        self.question_canvas.create_text(150, 125, width=300, text="Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2)

        self.window.mainloop()
