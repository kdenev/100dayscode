import turtle
import pandas as pd

states = pd.read_csv(r"day25\US States\50_states.csv")
guessed_states = list()

# Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"day25\US States\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

game_on = True

while game_on:

    answer_state = (screen.textinput(title=f"Guess the State ({len(guessed_states)}/{len(states['state'])})", prompt="What's another state's name?")).title()

    if answer_state == 'Exit':
        states_to_learn = states[~states['state'].isin(guessed_states)].state
        states_to_learn.to_csv(r"day25\US States\states_to_learn.csv", index=False)
        break

    if answer_state in states['state'].values and answer_state not in guessed_states:
        x_cor = states[states['state'] == answer_state]['x'].values[0]
        y_cor = states[states['state'] == answer_state]['y'].values[0]
        pen.goto(x_cor, y_cor)
        pen.write(answer_state)
        guessed_states.append(answer_state)

    if len(guessed_states) == len(states):
        game_on = False

screen.exitonclick()