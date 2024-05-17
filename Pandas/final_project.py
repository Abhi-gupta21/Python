from turtle import Screen, Turtle
import pandas

data = pandas.read_csv("day 25 pandas/50_states.csv")
answer_no = 0
screen = Screen()
screen.title("U.S. States Game")

screen.addshape("day 25 pandas/blank_states_img.gif")

turtle = Turtle()

turtle.shape("day 25 pandas/blank_states_img.gif")
gameon = True
while(gameon):
    answer = screen.textinput(title = "guess the state", prompt = "what's another state's name?")
    answer = answer.capitalize()
    if answer in data["state"].to_list():
        x = float(data[data["state"] == answer]['x'])
        y = float(data[data["state"] == answer]['y'])
        turtle2 = Turtle()
        turtle2.hideturtle()
        turtle2.penup()
        turtle2.goto(x,y)
        turtle2.pendown()
        turtle2.write(answer)
        print(answer)
        answer_no = answer_no + 1
        if answer_no == 50:
            gameon = False
            turtle3 = Turtle()
            turtle3.hideturtle()
            turtle3.penup()
            turtle3.goto(0,0)
            turtle3.pensize(3)
            turtle.pendown()
            turtle3.write("WELL DONE!! YOU GOT ALL THE STATES")


screen.mainloop()
        

# try improving it babe!

