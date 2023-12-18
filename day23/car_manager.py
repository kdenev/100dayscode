from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.cars = list()
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE
        

    def add_car(self):
        car = Turtle()
        car.penup()
        car.random_coordinate = random.choice(range(-220,221,5))
        car.setpos(280, car.random_coordinate)
        car.setheading(180)
        car.shape("square")
        car.shapesize(1,2)
        car.color(random.choice(COLORS))
        car.travel_speed = self.move_speed
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(car.travel_speed) 
    
    def speed_up(self):
        for car in self.cars:
            car.travel_speed += MOVE_INCREMENT
        self.move_speed += MOVE_INCREMENT
