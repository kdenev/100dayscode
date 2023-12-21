from turtle import Turtle

ALINGMENT = "center"
FONT = ("Arial", 24, "normal")
DEFAULT_POSITION = (0,260)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.up()
        self.speed("fastest")
        self.goto(DEFAULT_POSITION)
        self.hideturtle()
        self.color("white")
        self.print_score()
    
    def add(self):
        self.score += 1
        self.clear()
        self.goto(DEFAULT_POSITION)
        self.print_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", True, align=ALINGMENT, font=FONT)
        
    def print_score(self):
        self.clear()
        self.goto(DEFAULT_POSITION)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALINGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.print_score()

    def get_high_score(self):
        with open("day24\data.txt", "r") as h_score:
            self.high_score = int(h_score.read())

    def save_high_score(self):
        with open("day24\data.txt", "w") as h_score:
            h_score.write(str(self.high_score))

