from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = -125
for color in colors:
    turtle = Turtle("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-280, y_pos)
    y_pos += 50


screen.exitonclick()
