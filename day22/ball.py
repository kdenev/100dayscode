from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.turtlesize(stretch_len=1, stretch_wid=1)
        self.setheading(60)
        self.travel_speed = .1

    def bounce(self):
        self.hideturtle()
        bounce_angle = self.heading() - 45
        if bounce_angle < 0:
            bounce_angle += 360
        self.setheading(bounce_angle)
        self.showturtle()
    
    def reset_position(self):
        if self.xcor() > 400:
            new_dir = 180
        else:
            new_dir = 0
        self.setpos(0, 0)
        self.setheading(new_dir)
        
    def move(self):
        self.forward(20)
        
    def speed_up(self):
        self.travel_speed *= .9