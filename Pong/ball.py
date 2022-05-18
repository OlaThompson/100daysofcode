from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.09


    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.99

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.99



    def return_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.09

    def ball_speed(self):
        self.x_move += 5
        self.y_move += 5
