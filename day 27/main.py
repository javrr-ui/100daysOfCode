import tkinter

window = tkinter.Tk()
window.title("GUI Using Tkinter")
window.minsize(width=500, height=300)

label = tkinter.Label(text="A label")
label.pack()


# Button
def clicked():
    label["text"] = input.get()


button = tkinter.Button(text="Click me", command=clicked)
button.pack()

#Entry

input = tkinter.Entry(width=20)
input.pack()

window.mainloop()
