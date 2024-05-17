from turtle import Turtle
class snake():
    def __init__(self):
        self.tim = []
        for j in range(3):
            i = Turtle()
            i.penup()
            i.color('white')
            i.shape('square')
            i.goto(x=0-20*j, y=0)
            self.tim.append(i)
        self.score = 0

    def addtim(self):
        i = Turtle()
        i.penup()
        i.color('white')
        i.speed('fastest')
        i.shape('square')
        i.goto(self.tim[-1].position())
        self.tim.append(i)
        self.score += 1


    def move(self):
        for t in range(len(self.tim)-1,0,-1):

            x = self.tim[t-1].xcor()
            y = self.tim[t-1].ycor()
            self.tim[t].goto(x,y)
    
        self.tim[0].forward(20)

    def up(self):
        if self.tim[0].heading() != 270:
            self.tim[0].setheading(90)

    def down(self):
        if self.tim[0].heading() != 90:
            self.tim[0].setheading(270)
    
    def right(self):
        if self.tim[0].heading() != 180:
            self.tim[0].setheading(0)
    
    def left(self):
        if self.tim[0].heading() != 0:
            self.tim[0].setheading(180)

