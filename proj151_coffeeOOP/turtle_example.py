from turtle import Turtle, Screen
import time

tim = Turtle()
print(tim)
tim.shape('turtle')

tim.color('red', 'DarkOliveGreen1')

myscreen = Screen()
print(myscreen.canvheight)
for i in range(100):
    tim.forward(i*2)
    tim.tilt(i)
    tim.left(i)
    time.sleep(0.1)
myscreen.exitonclick()




