from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    pass


def move_backward():
    pass


def rotate_clockwise():
    pass


def rotate_counterclockwise():
    pass


def clear_screen():
    pass


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=rotate_counterclockwise, key="a")
screen.onkey(fun=rotate_clockwise, key="d")
screen.exitonclick()
