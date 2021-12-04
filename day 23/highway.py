from car import Car
from turtle import Turtle
from random import randrange


class Highway:
    def __init__(self, screen):
        self.highway_height = (screen.window_height() / 2) - 50
        self.highway_width = screen.window_width() / 2
        self.highway_limits()
        self.cars = []
        self.cars_speed = 5

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

    def fill(self):
        for y_position in range(-230, 250, 50):
            car = Car(x_pos=randrange(300, 800, 100), y_pos=y_position)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

            if car.xcor() < -self.highway_width - 50:
                car.hideturtle()
                self.cars.remove(car)
