import turtle
from turtle import Turtle
from random import choice, randint
from time import sleep
COLORS = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29),
          (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96),
          (15, 31, 22), (51, 55, 102), (159, 177, 54), (99, 44, 63), (35, 164, 196), (105, 44, 39), (164, 209, 187),
          (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]
LOC = []


class Car(Turtle):
    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.setheading(180)

    def colorize(self):
        self.color(choice(COLORS))

    def random_loc(self):
        self.goto(randint(320, 500),randint(-250, 280))

    def move(self):
        self.forward(20)