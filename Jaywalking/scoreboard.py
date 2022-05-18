from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_scoreboard()
        self.high_score = 1

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def reset(self):
        if self.level > self.high_score:
            self.high_score = self.level
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", "left",font= FONT)
        #self.write(f"Highest Level: {self.high_score}", "right", font= FONT)



