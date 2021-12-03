from car import Car
from turtle import Turtle


class Highway:
    def __init__(self, screen):
        self.highway_height = (screen.window_height()/2) - 50
        self.highway_width = screen.window_width() / 2
