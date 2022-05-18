from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.goto(-100, 235)
        self.updated_score()


    def updated_score(self):
        self.clear()
        self.goto(-100, 235)
        self.write(f"{self.paddle2_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(100, 235)
        self.write(f"{self.paddle1_score}", align="center", font=("Arial", 50, "normal"))


    def p1_point(self):
        self.paddle1_score += 1
        self.updated_score()


    def p2_point(self):
        self.paddle2_score += 1
        self.updated_score()