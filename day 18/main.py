from turtle import Turtle, Screen


def draw_square(turtle_obj):
    for _ in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)


turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "green")
draw_square(turtle)
screen = Screen()
screen.exitonclick()
