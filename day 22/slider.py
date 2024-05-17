from turtle import Turtle

class slider(Turtle):
    def __init__(self,string):
        super().__init__()
        self.speed('fastest')
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len = 5, stretch_wid = 1)
        self.penup()
        self.setheading(90)
        if string == 'left':
            self.goto(-395,0)
        else:
            self.goto(388,0)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)
    
