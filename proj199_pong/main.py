from constants import SCREEN_SIZE_WIDTH, SCREEN_SIZE_HEIGHT, SCREEN_SIZE_WIDE_MAX, SCREEN_SIZE_WIDE_MIN, SCREEN_SIZE_HEIGHT_MAX, SCREEN_SIZE_HEIGHT_MIN, POSITIONS
from ball import Ball
from midline import Midline
from scoreboard import Scoreboard
from paddle import Paddle


from turtle import Screen
import time


screen = Screen()
screen.setup(width=SCREEN_SIZE_WIDTH, height=SCREEN_SIZE_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
lp = Paddle(POSITIONS[1])
rp = Paddle(POSITIONS[2])
b = Ball()
m = Midline()
sc = Scoreboard()

game_running = True

screen.listen()
screen.onkey(rp.up, "Up")
screen.onkey(rp.down, "Down")
screen.onkey(lp.up, "w")
screen.onkey(lp.down, "s")

while game_running:
    time.sleep(0.05)
    screen.update()
    b.fly()

    # detect game over
    if sc.score['left'] >= 5 or sc.score['right'] >= 5:
        sc.game_over()
        game_running = False

    # detect collision to L and R walls
    if b.xcor() > SCREEN_SIZE_WIDE_MAX-10:
        sc.score_up('left')
        b.refresh()

    if b.xcor() < SCREEN_SIZE_WIDE_MIN+10: 
        sc.score_up('right')
        b.refresh()

    # detect collision to up and down walls
    if b.ycor() > SCREEN_SIZE_HEIGHT_MAX - 10 or b.ycor() < SCREEN_SIZE_HEIGHT_MIN + 10:
        b.reflect_walls()

    # detect collision to left paddle
    if abs(b.xcor() - lp.xcor()) < 10 and abs(b.ycor() - lp.ycor()) < 50:
        b.reflect_paddles()

    if abs(b.xcor() - rp.xcor()) < 10 and abs(b.ycor() - rp.ycor()) < 50:
        b.reflect_paddles()

screen.exitonclick()
