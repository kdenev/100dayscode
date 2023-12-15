from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

my_screen.update()

game_on = True
while game_on:

    my_screen.update()
    time.sleep(.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("snack")