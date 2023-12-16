from turtle import Screen
from paddle import Paddle

my_screen = Screen()
my_screen.window_width = 800
my_screen.window_height = 600
my_screen.bgcolor("black")
my_screen.title("PONG")


PADDLE_START_COR_X = 550
PADDLE_START_COR_Y = 0

paddle_R = Paddle(PADDLE_START_COR_X, PADDLE_START_COR_Y)
paddle_L = Paddle(-PADDLE_START_COR_X, PADDLE_START_COR_Y)


my_screen.listen()
my_screen.onkey(paddle_R.R_up, "Up")
my_screen.onkey(paddle_R.R_down, "Down")
my_screen.onkey(paddle_L.L_up, "w")
my_screen.onkey(paddle_L.L_down, "s")











my_screen.exitonclick()