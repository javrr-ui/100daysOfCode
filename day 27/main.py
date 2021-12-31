import tkinter

window = tkinter.Tk()
window.title("GUI Using Tkinter")
window.minsize(width=500, height=300)

label = tkinter.Label(text="A label")
label.grid(column=0, row=0)


# Button
def clicked():
    label["text"] = input.get()


button = tkinter.Button(text="Click me", command=clicked)
button.grid(column=1, row=0)

#Entry

input = tkinter.Entry(width=20)
input.grid(column=2, row=0)

window.mainloop()
