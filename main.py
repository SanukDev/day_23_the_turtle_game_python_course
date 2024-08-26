from turtle import Screen
from the_turtle import The_turtle
from car import Car
from time import sleep
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=800, height=600)

screen.listen()


screen.tracer(0)
scoreboard = Scoreboard()
the_turtle = The_turtle()
screen.onkey(key="Up", fun=the_turtle.move)
start_car = True
list_cars = []

while start_car:
    screen.update()
    sleep(the_turtle.time)
    random_choice = random.randint(1,6)
    if random_choice == 1:
        for x in range(1):
            cars = Car()
            cars.colorize()
            cars.random_loc()
            list_cars.append(cars)
    for cars in list_cars:
        cars.move()
        if the_turtle.distance(cars) < 25:
            scoreboard.game_over()
            start_car = False

    if the_turtle.ycor() > 290:
        the_turtle.pass_level()
        the_turtle.back_init()
        scoreboard.score()

screen.exitonclick()