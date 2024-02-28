from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self) -> None:
        self.length = 3
        self.turtle_array = []
        for i in range(self.length):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(POSITIONS[i])
            self.turtle_array.append(t)
        self.turtle_array[0].setheading(RIGHT)

    def move_forward(self) -> None:
        for i in range(len(self.turtle_array)-1, 0, -1):
            t = self.turtle_array[i]
            next_t = self.turtle_array[i-1]
            t.goto(next_t.xcor(), next_t.ycor())
        head = self.turtle_array[0]
        head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.turtle_array[0].heading() != DOWN:
            self.turtle_array[0].setheading(UP)

    def down(self) -> None:
        if self.turtle_array[0].heading() != UP:
            self.turtle_array[0].setheading(DOWN)

    def left(self) -> None:
        if self.turtle_array[0].heading() != RIGHT:
            self.turtle_array[0].setheading(LEFT)

    def right(self) -> None:
        if self.turtle_array[0].heading() != LEFT:
            self.turtle_array[0].setheading(RIGHT)
