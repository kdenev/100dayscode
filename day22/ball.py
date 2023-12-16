from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.turtlesize(stretch_len=1, stretch_wid=1)
        self.setheading(60)

    def bounce(self):
        bounce_angle = self.heading() - 90
        if bounce_angle < 0:
            bounce_angle += 360
        self.setheading(bounce_angle)
        
    def move(self):
        self.forward(30)
        