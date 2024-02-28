from turtle import Turtle
from constants import POSITIONS, RIGHT, LEFT, UP, DOWN, MOVE_DISTANCE



class Snake():
    def __init__(self) -> None:
        self.length = len(POSITIONS)
        self.turtle_array = []
        self.create_snake()
    
    def create_snake(self):
        self.length = len(POSITIONS)
        for i in range(self.length):
            t = Turtle("square")
            t.speed("fastest")
            t.color("white")
            t.penup()
            t.goto(POSITIONS[i])
            self.turtle_array.append(t)
        self.turtle_array[0].setheading(RIGHT)

    def reset(self):
        for t in self.turtle_array:
            t.goto(1000,1000)
        self.turtle_array.clear()
        self.create_snake()

    def grow(self) -> None:
        self.length += 1
        tail = self.turtle_array[-1]
        t = Turtle("square")
        t.speed("fastest")
        t.color("white")
        t.penup()
        t.goto(tail.xcor(), tail.ycor())
        self.turtle_array.append(t)

    def self_collision(self) -> bool:
        head_x = self.turtle_array[0].xcor()
        head_y = self.turtle_array[0].ycor()
        for i in range(1, len(self.turtle_array)):
            t = self.turtle_array[i]
            segment_x  = t.xcor()
            segment_y  = t.ycor()
            if abs(head_x - segment_x) <= 5 and abs(head_y - segment_y) <= 5:
                return True
        return False

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
