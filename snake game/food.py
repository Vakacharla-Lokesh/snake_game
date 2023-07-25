from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.new_food()

    def new_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(x=rand_x, y= rand_y)