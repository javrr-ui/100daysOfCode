import time
from turtle import Screen
from player import Player
from car import Car
from highway import Highway

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

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

