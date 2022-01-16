BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50)

card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_back)
canvas.grid(column=0, row=0, columnspan=2)
window.mainloop()
