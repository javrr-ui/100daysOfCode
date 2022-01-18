BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from pandas import *
from random import choice, shuffle
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

words = pandas.read_csv("data/french_words.csv")
words = words.to_dict(orient="records")

card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font="Arial 40 italic")
canvas.create_text(400, 263, text="Word", font="Arial 60 bold")
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)
window.mainloop()
