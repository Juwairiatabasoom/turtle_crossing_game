import turtle
from turtle import Turtle
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager():
    def __init__(self):
        self.car_speed=STARTING_MOVE_DISTANCE
        self.generates_cars()
        self.all_cars=[]


    def generates_cars(self):
        rand_int=random.randint(1,6)
        if rand_int==1: #to generate cars less frequently
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280,random.randint(-150,150))
            self.all_cars.append(new_car)

    def move_the_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed +=MOVE_INCREMENT








