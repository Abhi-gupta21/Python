from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width = 500, height = 400)
race_on = False
colors = ['red','green','black','orange','blue','purple']

userbet = screen.textinput(title= "Make your bet", prompt = f"these are the colors - {colors} which turtle will win the race? enter color - ")
tim = []
for i in range(6):
    newtim = Turtle()
    tim.append(newtim)

for i,j in zip(colors,range(6)):
    tim[j].penup()
    tim[j].shape('turtle')
    tim[j].color(i)
    tim[j].goto(x = -230, y = -180/2 + j*65/2)

if userbet:
    race_on = True

while race_on:
    for turtle in tim:
        dis = randint(0,10)
        turtle.forward(dis)
        if turtle.xcor() > 240:
            race_on = False
            winner = turtle


if str(winner.pencolor()).lower() == str(userbet).lower():
    print(f"your bet is {userbet.lower()} turtle, the winner is {winner.pencolor()} turtle, you won the bet!!")
else:
    print(f"your bet is {userbet.lower()} turtle, the winner is {winner.pencolor()} turtle, you lost the bet!!")


screen.exitonclick()