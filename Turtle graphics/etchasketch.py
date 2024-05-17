from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(1)

def move_backward():
    tim.backward(1)

def turn_clockwise():
    tim.right(1)

def turn_anticlockwise():
    tim.left(1)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key = 'Up', fun = move_forward)
screen.onkeypress(key = 'Down', fun = move_backward)
screen.onkeypress(key = 'Left', fun = turn_anticlockwise)
screen.onkeypress(key = 'Right', fun = turn_clockwise)
screen.onkey(key = 'c', fun = clear)
screen.exitonclick()