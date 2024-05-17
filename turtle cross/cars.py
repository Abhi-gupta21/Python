from turtle import Turtle
import random

color = ['red','green','white','yellow','blue','pink','orange']
class cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.goto(400, random.randint(-240,280))
        self.setheading(180)
        self.color(random.choice(color))

    

    def move(self): 
        self.forward(20)