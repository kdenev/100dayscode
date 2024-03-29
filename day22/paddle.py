from turtle import Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
TRAVEL_DISTANCE = 50


class Paddle(Turtle):
    def __init__(self, start_x, start_y) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.setpos(start_x, start_y)
        self.color("white")
        self.setheading(90)
        self.speed("fastest")
        
    def move(self):
        self.forward(TRAVEL_DISTANCE)

    def up(self):
        self.setheading(90)
        self.move()
        
    def down(self):
        self.setheading(270)
        self.move()