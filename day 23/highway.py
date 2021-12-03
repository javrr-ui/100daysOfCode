from car import Car
from turtle import Turtle


class Highway:
    def __init__(self, screen):
        self.highway_height = (screen.window_height()/2) - 50
        self.highway_width = screen.window_width() / 2
        self.highway_limits()

    def highway_limits(self):
        line = Turtle()
        line.penup()
        line.goto(self.highway_width, self.highway_height)
        line.pendown()
        line.goto(-self.highway_width, self.highway_height)
        line.penup()
        line.goto(self.highway_width, -self.highway_height)
        line.pendown()
        line.goto(-self.highway_width, -self.highway_height)