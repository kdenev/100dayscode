from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.starting_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.setpos(STARTING_POSITION)
    
