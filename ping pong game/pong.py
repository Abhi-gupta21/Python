from turtle import Screen, Turtle
import random
from ball import ball
from screendivide import screendivide
from slider import slider
from scoreb import scoreb

screen = Screen()
screen.tracer(0)
screendivide = screendivide()
screen.title('PONG')
screen.bgcolor('black')
screen.setup(height = 600, width = 800)
slider1 = slider('left')
slider2 = slider('right')
ball = ball()
p1score = scoreb(-200)
p2score = scoreb(200)
screen.update()

screen.listen()

screen.onkeypress(slider1.move_up, 'w')
screen.onkeypress(slider2.move_up, 'Up')
screen.onkeypress(slider1.move_down, 's')
screen.onkeypress(slider2.move_down, 'Down')
gameon = True

while gameon:
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        angle = ball.heading()
        ball.setheading(360 - angle)
    if slider1.distance(ball) < 50 and ball.xcor()<-370:
        ball.setheading(ball.heading() + random.randint(270,300))
    if slider2.distance(ball) < 50 and ball.xcor()>370:
        ball.setheading(ball.heading() + random.randint(270,300))
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.setheading(random.randint(0,360))
        p1score.updatescore()
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.setheading(random.randint(0,360))
        p2score.updatescore()

screen.exitonclick()