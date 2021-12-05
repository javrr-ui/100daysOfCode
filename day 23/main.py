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
highway.fill()
screen.onkeypress(player.move_up, "w")
loop_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    if loop_count % 70 == 0:
        highway.fill()
    highway.move_cars()
    screen.update()
    loop_count += 1

    for car in highway.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > highway.highway_height:
        player.reset_position()
        highway.increase_speed()
        scoreboard.level_up()
scoreboard.game_over()
screen.exitonclick()
