from turtle import Turtle

class tim(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-270)
        self.color('white')
        self.shape('turtle')
        self.setheading(90)
