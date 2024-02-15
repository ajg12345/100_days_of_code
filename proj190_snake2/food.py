from turtle import Turtle
from constants import SCREEN_SIZE_MAX, SCREEN_SIZE_MIN
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(SCREEN_SIZE_MIN+20, SCREEN_SIZE_MAX-20)
        random_y = random.randint(SCREEN_SIZE_MIN+20, SCREEN_SIZE_MAX-20)
        self.goto(random_x, random_y)