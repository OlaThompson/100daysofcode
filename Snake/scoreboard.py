from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 460)
        self.updated_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updated_score()

    def updated_score(self):
        self.write(f"Score:{self.score}", align="right", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="right", font=("Arial", 20, "normal"))