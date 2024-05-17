from turtle import Turtle
import random
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setheading(random.randint(0,360))

    def move_ball(self):
        self.forward(0.2)
