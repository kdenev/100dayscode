import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
cars = CarManager()
cars.add_car()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    # Cars
    if random.random() > .8:
        cars.add_car()
    cars.move()
    # Score
    score.update_score()
    if player.ycor() > 280:
        score.count_score()
        player.starting_position()
        cars.speed_up()
    # Detect collision
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    screen.update()

screen.exitonclick()