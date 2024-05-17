from turtle import Turtle

class screendivide(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-300)
        self.hideturtle()
        for i in range(30):
            self.color('white')
            self.pendown()
            self.setheading(90)
            self.forward(10)
            self.penup()
            self.forward(10)

