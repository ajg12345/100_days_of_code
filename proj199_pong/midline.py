import math
from turtle import Turtle

from constants import SCREEN_SIZE_HEIGHT_MAX

class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, SCREEN_SIZE_HEIGHT_MAX)
        self.hideturtle()
        self.setheading(270)
        for _ in range(math.ceil(2*SCREEN_SIZE_HEIGHT_MAX/20)):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)