from turtle import Turtle, Screen, colormode
import random

colormode(255)
my_screen = Screen()
my_screen.setup(width=500, height=400)
u_bet = my_screen.textinput(title="Make your bet", prompt="Which T will win the race? Enter a color: ")
print(u_bet)

turtles = list()
start_y = list(range(-100,151,50))

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

for n in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[n].color(colors[n])
    turtles[n].up()
    turtles[n].goto(x=-230, y=start_y[n])

is_race_on = False

if u_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() >= 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == u_bet:
                print(f"You win! Winner turtle: {winning_color}")
                winning_color
            else:
                print(f"You lose! Winner turtle: {winning_color}")
                break
        t.forward(random.randint(10,30))

my_screen.exitonclick()
