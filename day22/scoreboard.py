from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def count_score(self, ball):
        if ball.xcor() > 0:
            self.l_score += 1
        else:
            self.r_score += 1