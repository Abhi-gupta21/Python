from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align = "center", font = ("Arial", 20, "normal"))

    def gameover(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = ("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

        
