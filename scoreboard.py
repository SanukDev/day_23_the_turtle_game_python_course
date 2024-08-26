from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score_l = 1
        self.score_level()

    def score_level(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Level {self.score_l}",align="center", font=("Arial", 30, "normal"))

    def score(self):
        self.score_l += 1
        self.score_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 50, "normal"))