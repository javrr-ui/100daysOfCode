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


def random_walk(turtle_obj):
    direction = random.randint(1, 4)
    if direction == 1:
        turtle_obj.forward(30)
    elif direction == 2:
        turtle_obj.left(90)
        turtle_obj.forward(30)
    elif direction == 3:
        turtle_obj.right(90)
        turtle_obj.forward(30)
    elif direction == 4:
        turtle_obj.backward(30)


def draw_circle(turtle_obj, radius, heading_angle):
    turtle_obj.circle(radius)
    turtle_obj.setheading(heading_angle)


turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "green")
turtle.speed(0)
# Turtle Challenge 4
# turtle.pensize(10)
# while True:
#     set_random_color(turtle)
#     random_walk(turtle)

# Turtle Challenge 3
# for sides in range(3, 11):
#     draw_figure(turtle, sides)

# Turtle Challenge 2
# draw_dashed_line(turtle)

# Turtle Challenge 1
# draw_square(turtle)

screen = Screen()
screen.colormode(1)
screen.exitonclick()
