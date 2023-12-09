from turtle import Turtle, Screen

t1 = Turtle()
t1.shape("circle")
t1.color("lightblue")

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

draw_dash_line(t1, 100)

my_screen = Screen()
my_screen.exitonclick()