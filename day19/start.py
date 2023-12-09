from turtle import Turtle, Screen


t1 = Turtle()

def move_forward():
    t1.forward(10)

def move_backward():
    t1.backward(10)

def turn_right():
    t1.right(10)

def turn_left():
    t1.left(10)

def clear_screen():
    t1.clear()
    t1.up()
    t1.home()
    t1.down()

my_screen = Screen()
my_screen.listen()


my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backward, key="s")
my_screen.onkey(fun=turn_right, key="d")
my_screen.onkey(fun=turn_left, key="a")
my_screen.onkey(fun=clear_screen, key="c")

my_screen.exitonclick()
