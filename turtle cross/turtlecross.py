from turtle import Screen
from cars import cars
from tim import tim
import time

def movecontinously(carss):
    for c in carss:
        c.move()

screen = Screen()
screen.setup(height = 600, width = 800)
screen.tracer(0)
screen.bgcolor('black')

timm = tim()
carss = []
car = cars()
carss.append(car)
gameon = True

while gameon:
    time.sleep(1.5)
    screen.update()
    car = cars()
    movecontinously(carss)
    carss.append(car)


screen.exitonclick()