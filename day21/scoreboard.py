from turtle import Turtle

ALINGMENT = "center"
FONT = ("Arial", 24, "normal")
DEFAULT_POSITION = (0,260)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
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
        self.write(f"Score: {self.score}", True, align=ALINGMENT, font=FONT)
