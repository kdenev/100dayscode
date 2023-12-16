from turtle import Screen
from paddle import Paddle
from ball import Ball
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

my_screen.listen()
my_screen.onkey(paddle_R.up, "Up")
my_screen.onkey(paddle_R.down, "Down")
my_screen.onkey(paddle_L.up, "w")
my_screen.onkey(paddle_L.down, "s")

game_on = True

while game_on:
    # ball.goto(350, 250)
    time.sleep(.2)
    ball.move()
    my_screen.update()




my_screen.exitonclick()