from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
y_coordinates = []
for number in range (-230,230,20):
    y_coordinates.append(number)



class CarManager:
    def __init__(self):
       self.all_cars = []
       self.speed = STARTING_MOVE_DISTANCE

    def game_car(self):
        frequency = random.randint(1,6)
        if frequency == 1:
          next_car = Turtle("square")
          next_car.shape("square")
          next_car.shapesize(1,2)
          next_car.color(random.choice(COLORS))
          next_car.setheading(180)
          next_car.penup()
          next_car.goto(300,random.choice(y_coordinates))
          self.all_cars.append(next_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT




