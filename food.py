from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7,0.7)
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        x = random.randint(-750,750)
        y = random.randint(-480,480)
        self.goto(x,y)