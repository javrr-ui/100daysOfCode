import tkinter

window = tkinter.Tk()
window.title("GUI Using Tkinter")
window.minsize(width=500, height=300)

label = tkinter.Label(text="A label")
label.pack()
window.mainloop()