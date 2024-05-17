from turtle import Turtle, Screen
from snake import snake
from scoreboard import scoreboard
from food import food
import time
import random

pamu = snake()
food = food()
scoreboard = scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()



gameon = True



screen.onkey(pamu.up, "Up")
screen.onkey(pamu.down, "Down")
screen.onkey(pamu.left, "Left")
screen.onkey(pamu.right, "Right")





while gameon:
    screen.update()
    time.sleep(0.14)
    pamu.move()

        
    if pamu.tim[0].distance(food) < 15:
        food.refresh()
        pamu.addtim()
        scoreboard.update_score()
    
    if pamu.tim[0].xcor()>280 or pamu.tim[0].xcor()<-280 or pamu.tim[0].ycor()>280 or pamu.tim[0].ycor()<-280:
        gameon = False
        scoreboard.gameover()

    for t in pamu.tim[1:]:
        if pamu.tim[0].distance(t) < 10:
            gameon = False
            scoreboard.gameover()
    
screen.exitonclick()

print(f"Good job! your final score - {pamu.score}")