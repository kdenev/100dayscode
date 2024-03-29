from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("PONG")
my_screen.tracer(0)


PADDLE_START_COR_X = 350
PADDLE_START_COR_Y = 0

paddle_R = Paddle(PADDLE_START_COR_X, PADDLE_START_COR_Y)
paddle_L = Paddle(-PADDLE_START_COR_X, PADDLE_START_COR_Y)
ball = Ball()
score = Scoreboard() 

my_screen.listen()
my_screen.onkey(paddle_R.up, "Up")
my_screen.onkey(paddle_R.down, "Down")
my_screen.onkey(paddle_L.up, "w")
my_screen.onkey(paddle_L.down, "s")

game_on = True

while game_on:
    # ball.goto(350, 250)
    time.sleep(ball.travel_speed)
    ball.move()
    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
    # Paddle collision
    if (ball.distance(paddle_L) < 50 and ball.xcor() < -300) or (ball.distance(paddle_R) < 50 and ball.xcor() > 300):
        ball.bounce()
        ball.speed_up()
    # Score
    if ball.xcor() > 380 or ball.xcor() < -380:
        score.count_score(ball)
        ball.reset_position()
        score.update_scoreboard()
        
        
    my_screen.update()
    


my_screen.exitonclick()