from snake import Snake

from turtle import Screen
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
s = Snake()

game_running = True

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

while game_running:
    screen.update()
    time.sleep(0.1)
    s.move_forward()

screen.exitonclick()
