from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0

    def count_score(self):
        self.score +=1

    def update_score(self):
        self.clear()
        self.setpos(-280, 260)
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.setpos(0, 260)
        self.write(f"GAME OVER", font=FONT)