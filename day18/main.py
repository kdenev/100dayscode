from colorgram import extract
import random
from turtle import Turtle, Screen, setworldcoordinates,colormode

colors = [tuple(x.rgb) for x in extract('day18\image.jpeg', number_of_colors=-1)][4:]
colormode(255)
setworldcoordinates(-50,-50, 500, 500)

t1 = Turtle()
t1.speed("fastest")

def draw_row(t1:Turtle, colors):
    for _ in range(10):
        t1.dot(20, random.choice(colors))
        t1.up()
        t1.forward(50)
        t1.down()

def row_up(t1:Turtle):
    y = t1.position()[1] + 50 
    t1.up()
    t1.goto(0,y)
    t1.down()

t1.hideturtle()

for _ in range(10):
    draw_row(t1, colors)
    row_up(t1)

my_screen = Screen()
my_screen.exitonclick()