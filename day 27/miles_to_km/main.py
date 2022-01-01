from tkinter import *


def convert():
    miles = float(miles_entry.get())
    kilometers = miles * 1.609
    km.config(text=str(kilometers))


window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

km = Label(text="0")
km.grid(column=1, row=1)

button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

window.mainloop()
