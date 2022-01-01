from tkinter import *

window = Tk()
window.title("Mile to Km converter")

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

window.mainloop()
