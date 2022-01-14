from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    new_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    data = {}
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something is wrong", message="Please don't leave any fields empty!")
    else:
        save_data = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}\n"
                                                                  f"Password: {password}\nIs it ok to save?")
        if save_data:
            try:
                with open("data.json", "r") as file:
                    try:
                        data = json.load(file)
                    except JSONDecodeError:
                        pass
            except FileNotFoundError:
                file = open("data.json", "w")
                file.close()

            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------- SEARCH -------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            pass
    except FileNotFoundError:
        messagebox.showinfo("Error", message="No data file found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=34)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
