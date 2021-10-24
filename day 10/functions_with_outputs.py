#Functions with outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Invalid input"

    return f"{f_name} {l_name}".title()

f_name = input("What's your first name? ")
l_name = input("What's yout last name? ")


print(format_name(f_name, l_name))