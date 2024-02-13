from turtle import Turtle, Screen
import time
import random

def draw_square(tim):
    for i in range(4):
        tim.forward(100)
        tim.left(90)
        time.sleep(1)

def draw_shape(tim, num_of_sides):
    angle = round(360 / num_of_sides)
    length = 100
    for i in range(num_of_sides):
        tim.forward(length)
        tim.left(angle)
        time.sleep(.2)

def dotted_line(tim):
    for i in range(100):
        tim.pendown()
        tim.forward(2)
        tim.penup()
        tim.forward(2)

def random_walk(tim, steps):
    scale = 5
    tim.speed('fastest')
    tim.width(2*scale)
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        color_tuple = (random.randrange(0, 255),random.randrange(0, 255), random.randrange(0, 255))

        tim.pencolor(color_tuple)
        tim.forward(4*scale)
        tim.setheading(random.choice(directions))
        time.sleep(.2)

def spirograph(tim):
    for _ in range(36):
        color_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.pencolor(color_tuple)
        tim.circle(100)
        tim.right(10)



if __name__ == "__main__":
    
    tim = Turtle()
    myscreen = Screen()
    myscreen.colormode(255)
    
    
    # turtle characteristics
    tim.speed(9)
    spirograph(tim)
    myscreen.exitonclick()
    myscreen.mainloop()
    #random_walk(tim, 100)
    
    
    # for i in range(3,10):
        # draw_shape(tim, i)
    
    




