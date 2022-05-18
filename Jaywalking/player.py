from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.shape("turtle")
        self.color("brown")
        self.penup()
        self.start()
        self.showturtle()

    def move (self):
        self.forward(MOVE_DISTANCE)
    def start(self):
        self.goto(0, -280)