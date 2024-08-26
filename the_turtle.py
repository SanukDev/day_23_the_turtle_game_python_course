from turtle import Turtle


class The_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.time = 0.1

    def move(self):
        self.forward(10)

    def back_init(self):
        self.goto(0, -280)

    def pass_level(self):
        self.time -= 0.02
