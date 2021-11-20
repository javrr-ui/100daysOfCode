from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


food = Food()
snake = Snake(0, 0)
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
while True:
    screen.update()
    time.sleep(0.10)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
