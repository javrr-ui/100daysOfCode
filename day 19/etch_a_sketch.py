from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def rotate_clockwise():
    turtle.setheading(turtle.heading() - 10)


def rotate_counterclockwise():
    turtle.setheading(turtle.heading() + 10)


def clear_screen():
    turtle.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=rotate_counterclockwise, key="a")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
