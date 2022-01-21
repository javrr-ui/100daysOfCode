from tkinter import *
from pandas import *
from random import choice, shuffle

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

words = pandas.read_csv("data/french_words.csv")
word_count = len(words)
words = words.to_dict(orient="records")
shuffle(words)
word_index = 0


def new_card():
    window.after_cancel(after)
    global word_index
    word_index += 1
    if not word_index < word_count:
        word_index = 0
    hide_card()
    wait()


def show_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(word, text=words[word_index].get("English"), fill="white")
    canvas.itemconfig(title, text="English", fill="white")


def hide_card():
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(word, text=words[word_index].get("French"), fill="black")
    canvas.itemconfig(title, text="French", fill="black")


def wait():
    global after
    after = window.after(3000, show_card)


card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="French", font="Arial 40 italic")
word = canvas.create_text(400, 263, text=words[0].get("French"), font="Arial 60 bold")
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, command=new_card)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR, command=new_card)
right_button.grid(column=1, row=1)

wait()

window.mainloop()
