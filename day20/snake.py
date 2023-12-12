from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, starting_positions = STARTING_POSITIONS) -> None:
        self.starting_positions = starting_positions
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in self.starting_positions:
            t = Turtle()
            t.up()
            t.shape("square")
            t.color("white")
            t.setpos(position)
            self.snake.append(t)
    
    def move(self, dist = MOVE_DISTANCE):

        for t_num in range(len(self.snake) - 1, 0 ,-1):
            
            new_x = self.snake[t_num - 1].xcor()
            new_y = self.snake[t_num - 1].ycor()
            self.snake[t_num].setpos(new_x, new_y)

        self.head.forward(dist)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
