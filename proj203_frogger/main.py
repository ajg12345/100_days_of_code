import time
from turtle import Screen

from car_manager import CarManager
from constants import SCREEN_SIZE_HEIGHT, SCREEN_SIZE_WIDTH, FINISH_LINE_Y
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=SCREEN_SIZE_WIDTH, height=SCREEN_SIZE_HEIGHT)
screen.tracer(0)

p = Player()
sb = Scoreboard()
cm = CarManager()

screen.listen()
screen.onkey(p.up, "Up")
screen.onkey(p.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #check if turtle crossed road, then reset him
    if p.ycor() >= (FINISH_LINE_Y):
        sb.level_up()
        p.refresh()
        cm.increase_level_speed()

    cm.move_cars()

    # check if a car ran over the player
    for car in cm.car_list:
        if abs(p.ycor() - car.ycor()) < 15 and p.distance(car) < 20:
            sb.game_over()
            game_is_on = False

screen.exitonclick()



