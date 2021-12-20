import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()
text.penup()

while True:
    answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer = answer.title()

    data = pandas.read_csv("50_states.csv")
    state = data[data["state"] == answer]

    if answer in list(state["state"]):
        x = state["x"].item()
        y = state["y"].item()
        text.goto(x, y)
        text.write(answer, align="center", font=("Arial", 8, "normal"))

turtle.mainloop()
