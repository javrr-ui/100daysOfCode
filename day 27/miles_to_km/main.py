from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

window.mainloop()
