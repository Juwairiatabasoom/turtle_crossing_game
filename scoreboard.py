FONT = ("Courier", 18, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.write(f"Level:{self.level}",align="center",font=FONT)

    def increase_level(self):
        self.level+=1
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)


    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER",align="CENTER",font=("Courier", 32, "normal"))







