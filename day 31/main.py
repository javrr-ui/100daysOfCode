BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_back)
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)
window.mainloop()
