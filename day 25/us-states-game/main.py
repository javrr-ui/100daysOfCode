import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()
text.penup()
user_states = []
data = pandas.read_csv("50_states.csv")
missing_states = data["state"].to_list()

while True:
    answer = screen.textinput(title=f"{len(user_states)}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()

    state = data[data["state"] == answer]

    if answer == "Exit":
        break

    if answer in list(state["state"]):
        x = state["x"].item()
        y = state["y"].item()
        text.goto(x, y)
        text.write(answer, align="center", font=("Arial", 8, "normal"))
        user_states.append(answer)
        missing_states.remove(answer)

missing_states_dict = {
    "missing states": missing_states
}
df = pandas.DataFrame(missing_states_dict)
df.to_csv("missing_states.csv")
