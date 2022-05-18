from turtle import Turtle, Screen
import random

t_turtle = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=500)
user_input = screen.textinput(title="Turtle bet race", prompt="What color of turtle will win the race?\n:")
color = ["red", "orange", "yellow", "green", "blue", "black", "purple"]
positions = [-70, -30, 10, 50, 90, 130, 170]
is_race_on = False
race_drivers = []

for racer_position in range(0, 7):
    new_racer = Turtle(shape="turtle")
    new_racer.penup()
    new_racer.color(color[racer_position])
    new_racer.goto(x=-230, y=positions[racer_position])
    race_drivers.append(new_racer)
if user_input:
    is_race_on = True
while is_race_on:

    for racers in race_drivers:
        if racers.xcor() > 230:
            is_race_on = False
            winning_racer = racers.pencolor()
            if winning_racer == user_input:
                print(f"You won your bet! Racer {winning_racer} won the race.")
            else:
                print(f"You lost! Racer {winning_racer} won the race. ")
        racers.forward(random.randint(0, 10))


screen.exitonclick()