import time
from turtle import Screen
from player import Player
from highway import Highway
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
highway = Highway(screen)
screen.onkeypress(player.move_up, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    highway.move_cars()
    screen.update()

    for car in highway.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > highway.highway_height:
        player.reset_position()
        highway.increase_speed()
        scoreboard.level_up()
scoreboard.game_over()
screen.exitonclick()
