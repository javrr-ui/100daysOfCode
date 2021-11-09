from turtle import Turtle, Screen


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


turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "green")
draw_square(turtle)
draw_dashed_line(turtle)
screen = Screen()
screen.exitonclick()
