from turtle import Turtle, Screen, colormode
import random


colormode(255)

t1 = Turtle()
t1.shape("circle")
t1.color("lightblue")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)


def draw_square(t: Turtle, side: int):
    for _ in range(4):
        t.forward(side)
        t.left(90)
        
# draw_square(t1,300)

def draw_dash_line(t: Turtle, l: int):
    for _ in range(round(l//10)):
        t.up()
        t.forward(l//10)
        t.down()
        t.forward(l//10)

# draw_dash_line(t1, 100)

def draw_form(t: Turtle, n: int, side: int):
    t.color(random_color())
    for _ in range(n):
        t.forward(side)
        t.left(360/n)
        

colors = ["red", "blue", "green", "yellow", "black"]

# for n in range(3,9):
#     draw_form(t1, n, 100, colors)

def draw_random_wald(t: Turtle, steps: int, w:int, s:int):
    t.speed(s)
    t.width(w)
    turn_angles = list(range(0,271, 90))
    for _ in range(steps):
        t.color(random_color())
        t.setheading(random.choice(turn_angles))
        t.forward(random.randint(50,100))

# draw_random_wald(t1, 100, 15, 20)

def draw_spirograph(t: Turtle, tilt: int):
    t.color(random_color())
    t.speed("fastest")
    tilt = 0
    while round(tilt,0) != 360:
        t.setheading(tilt)
        t.color(random_color())
        t.circle(radius=100)
        tilt += 10

draw_spirograph(t1, 26)

my_screen = Screen()
my_screen.exitonclick()