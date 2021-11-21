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

scoreboard = Scoreboard()
food = Food()
snake = Snake(0, 0)
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.10)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.lengthen()
        food.refresh()
        scoreboard.add_point()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        scoreboard.game_over()
        print("You lose!")
        print(f"Final score: {scoreboard.score}")
        break

    if snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        scoreboard.game_over()
        print("You lose!")
        print(f"Final score: {scoreboard.score}")
        break

screen.exitonclick()
