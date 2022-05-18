from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)
game_is_on = True
paddle2 = Paddle((-370,0))
paddle1 = Paddle((370,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.distance(paddle1) < 50 and ball.xcor()>340:
        ball.bounce_x()

    elif ball.distance(paddle2) < 50 and ball.xcor()<-340:
        ball.bounce_x()


    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    elif ball.xcor() >390:
        ball.return_position()
        scoreboard.p2_point()

    elif ball.xcor() < -390:
        ball.return_position()
        scoreboard.p1_point()


screen.exitonclick()