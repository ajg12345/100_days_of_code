from constants import COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT, SCREEN_SIZE_WIDE_MIN, SCREEN_SIZE_WIDE_MAX, SCREEN_SIZE_HEIGHT_MAX, SCREEN_SIZE_HEIGHT_MIN, STARTING_CAR_COUNT

from turtle import Turtle
from random import choice, randint


class CarManager():
    def __init__(self):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_count = STARTING_CAR_COUNT
        for i in range(self.car_count):
            self.create_car()

    def increase_level_speed(self):
        self.move_distance += MOVE_INCREMENT
        for i in range(3):
            self.create_car()

    def create_car(self):
        c = Turtle("square")
        c.color(choice(COLORS),choice(COLORS))
        c.seth(180)
        c.shapesize(stretch_len=2, stretch_wid=1)
        c.penup()
        self.reset_car(c, True)
        self.car_list.append(c)

    def reset_car(self, car, initial:bool = False):
        if initial:
            starting_positing_x = randint(SCREEN_SIZE_WIDE_MIN, SCREEN_SIZE_WIDE_MAX)
        else:
            starting_positing_x = 300
        starting_position_y = randint(SCREEN_SIZE_HEIGHT_MIN + 30, SCREEN_SIZE_HEIGHT_MAX)
        starting_position = (starting_positing_x, starting_position_y)
        car.goto(starting_position)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.move_distance)
            if car.xcor() <= SCREEN_SIZE_WIDE_MIN:
                self.reset_car(car)
