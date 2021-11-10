from turtle import Turtle, Screen
import random


def draw_square(turtle_obj):
    for _ in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)


def draw_dashed_line(turtle_obj):
    for _ in range(15):
        turtle_obj.forward(10)
        turtle_obj.penup()
        turtle_obj.forward(10)
        turtle_obj.pendown()


def draw_figure(turtle_obj, number_of_sides):
    set_random_color(turtle_obj)
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        turtle_obj.forward(100)
        turtle_obj.right(angle)


def set_random_color(turtle_obj):
    turtle_obj.pencolor(random.random(), random.random(), random.random())


turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "green")
# draw_square(turtle)
# draw_dashed_line(turtle)
screen = Screen()
screen.colormode(1)
screen.exitonclick()
