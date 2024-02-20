import math
import random
from turtle import Turtle

from constants import POSITIONS

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.refresh()
        self.radians()

    def refresh(self):
        self.goto(POSITIONS[0])
        self.setheading(random.randint(0, math.floor(2*math.pi)))

    def fly(self, speed=10):
        self.forward(speed)

    def reflect_walls(self):
        alpha = self.heading() # pi/3
        self.setheading(2*math.pi - alpha)

    def reflect_paddles(self):
        alpha = self.heading() # pi/3
        self.setheading(math.pi - alpha)