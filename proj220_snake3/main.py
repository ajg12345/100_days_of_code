from constants import SCREEN_SIZE_WIDTH, SCREEN_SIZE_LENGTH, SCREEN_SIZE_MAX, SCREEN_SIZE_MIN
from food import Food
from snake import Snake
from scoreboard import Scoreboard

from turtle import Screen
import time




screen = Screen()
screen.setup(width=SCREEN_SIZE_WIDTH, height=SCREEN_SIZE_LENGTH)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
s = Snake()
f = Food()
sc = Scoreboard()

game_running = True

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

def game_over():
    screen.textinput(title="LOSER", prompt=f"YOUR SCORE IS {s.length}")
    return False


while game_running:
    screen.update()
    time.sleep(0.1)
    s.move_forward()

    # detect collision from food
    if s.turtle_array[0].distance(f) < 15:
        sc.score_up()
        s.grow()
        f.refresh()
        # add code to make snake longer

    # detect collision to wall
    if s.turtle_array[0].xcor() > SCREEN_SIZE_MAX-10 or s.turtle_array[0].xcor() < SCREEN_SIZE_MIN+10 \
        or s.turtle_array[0].ycor() > SCREEN_SIZE_MAX-10 or s.turtle_array[0].ycor() < SCREEN_SIZE_MIN+10:
        sc.reset()
        s.reset()

    # detect collision to self
    if s.self_collision():
        sc.reset()
        s.reset()



screen.exitonclick()
