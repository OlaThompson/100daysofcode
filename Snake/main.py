from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("3310 Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.3)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()

    elif snake.head.xcor() < -480 or snake.head.xcor() >480 or snake.head.ycor() > 480 or snake.head.xcor() < -480:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()