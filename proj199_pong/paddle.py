from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self) -> None:
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self) -> None:
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)