from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "normal"))
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250)
        self.question_text = self.question_canvas.create_text(150, 125, width=300, text="Text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=lambda: self.check_answer("True"))
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=lambda:  self.check_answer("False"))
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        self.question_canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def check_answer(self, user_answer):
        is_right = self.quiz.check_answer(user_answer)
        self.update_score()
        self.give_feedback(is_right)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
