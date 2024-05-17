from turtle import Turtle

class scoreb(Turtle):
    def __init__(self,x):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x,250)
        self.pendown()
        self.hideturtle()
        self.write(f'score = {self.score}')

    def updatescore(self):
        self.score += 1
        self.clear()
        self.write(f'score = {self.score}')

    