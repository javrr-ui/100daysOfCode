import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()

answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
answer = answer.title()

data = pandas.read_csv("50_states.csv")
state = data[data["state"] == answer]

turtle.mainloop()
