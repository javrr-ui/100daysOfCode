from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
message = f"Available turtles: {', '.join(colors)}\n\n Which turtle will win the race? Enter a color: "
user_bet = screen.textinput(title="Make your bet", prompt=message)

turtles = []
y_pos = -125
for color in colors:
    turtle = Turtle("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-280, y_pos)
    y_pos += 50
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() >= (screen.window_width() / 2) - 30:
            is_race_on = False
            if turtle.fillcolor() == user_bet:
                print(f"You've won! The {turtle.fillcolor()} turtle is the Winner")
            else:
                print(f"You've lost! The {turtle.fillcolor()} turtle is the Winner")
            break


screen.exitonclick()
