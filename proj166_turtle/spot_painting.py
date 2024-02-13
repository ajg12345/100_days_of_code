import colorgram
from turtle import Turtle, Screen
import time
from random import choice

colors = colorgram.extract('hirst_painting.jpg', 10)
rgb_colors = []
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))


def get_matrix() -> list:
    return [(x, y) for x in range(-250, 250, 50) for y in range(-250, 250, 50)]
    
def draw_dot(tim, color):
    tim.dot(20, color)

if __name__ == "__main__":
    """
    10x10 dot matrix
    each dot is 20 diameter
    each spaced 50 apart
    """
    tim = Turtle()
    myscreen = Screen()
    myscreen.colormode(255)
    
    # get colors
    colors = colorgram.extract('hirst_painting.jpg', 10)
    rgb_colors = []
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    # turtle characteristics
    tim.speed(9)
    # method
    matrix = get_matrix()
    for point in matrix:
        tim.penup()
        tim.setx(point[0])
        tim.sety(point[1])
        tim.pendown()
        draw_dot(tim, choice(rgb_colors))
        time.sleep(0.2)
    myscreen.exitonclick()
    myscreen.mainloop()