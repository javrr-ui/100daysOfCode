from tkinter import *
from pandas import *
from random import choice, shuffle

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except:
    words = pandas.read_csv("data/french_words.csv")
    words.to_csv("data/words_to_learn.csv", index=False)

words = words.to_dict(orient="records")
shuffle(words)


def new_card(button_pressed):
    try:
        window.after_cancel(after)
    except:
        pass

    if button_pressed == "right_button" and len(words) > 0:
        try:
            df = pandas.read_csv("data/words_to_learn.csv")
            df.drop(df[df["English"] == words[0].get("English")].index, inplace=True)
            df.to_csv("data/words_to_learn.csv", index=False)
            # Remove word from list AFTER removing it from dataFrame
            words.remove(words[0])
            hide_card()
            wait()
        except IndexError:
            pass


def show_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(word, text=words[0].get("English"), fill="white")
    canvas.itemconfig(title, text="English", fill="white")


def hide_card():
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(word, text=words[0].get("French"), fill="black")
    canvas.itemconfig(title, text="French", fill="black")


def wait():
    global after
    after = window.after(3000, show_card)


card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)

canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, command=lambda m="wrong_button": new_card(m))
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR, command=lambda m="right_button": new_card(m))
right_button.grid(column=1, row=1)

try:
    word = canvas.create_text(400, 263, text=words[0].get("French"), font="Arial 60 bold")
    title = canvas.create_text(400, 150, text="French", font="Arial 40 italic")
    wait()
except IndexError:
    title = canvas.create_text(400, 150, text="", font="Arial 40 italic")
    word = canvas.create_text(400, 263, text="", font="Arial 60 bold")

window.mainloop()
