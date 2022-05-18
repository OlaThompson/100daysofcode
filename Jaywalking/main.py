import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Jaywalking")
screen.tracer(0)
screen.onkey(player.move,"Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.game_car()
    cars.move_car()
    for car in cars.all_cars:
        if car.distance(player)< 20:
            scoreboard.reset()
    if player.ycor() > 230:
        player.start()
        cars.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()