import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
answer = answer.title()

turtle.mainloop()
