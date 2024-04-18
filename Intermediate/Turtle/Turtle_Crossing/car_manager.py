from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        
    def generate_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            color = random.choice(COLORS)
            new_y = random.randint(-250,250)
            car = Turtle()
            car.color(color)
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid= 1, stretch_len= 2)
            car.goto(280, new_y)
            car.setheading(180)
            self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
            
    def update_speed(self):
        self.move_distance += MOVE_INCREMENT
        
            