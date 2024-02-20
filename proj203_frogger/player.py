
from constants import STARTING_POSITION, MOVE_DISTANCE, FINISH_LINE_Y
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.refresh()

    def refresh(self) -> None:
        self.goto(STARTING_POSITION)
        self.seth(90)

    def up(self)-> None:
        self.forward(MOVE_DISTANCE)

    def down(self)-> None:
        self.forward(-MOVE_DISTANCE)

    def is_winner(self)-> None:
        return self.ycor() >= FINISH_LINE_Y
