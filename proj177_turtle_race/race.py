from turtle import Turtle, Screen
import random

if __name__ == "__main__":
    """
    W forward 10
    S backward 10
    A counter clockwise
    D clockwise
    C clear drawing
    """
    
    myscreen = Screen()
    myscreen.setup(width=500, height=400)
    userbet = myscreen.textinput(title="whats your bet?", prompt="which turtle will win the race? (type color)")
    myscreen.colormode(255)
    
    turtle_list = []
    color_list = ['red']#, 'orange', 'yellow', 'green', 'blue', 'purple']
    starting_position = (-230, 50)
    x = -230
    y = 50
    for color in color_list:
        t = Turtle(shape='turtle')
        t.color(color)
        t.penup()
        
        t.goto(x, y)
        turtle_list.append(t)
        y -= 20
    race = True
    while race:
        for turtle in turtle_list:
            movement = random.randint(0, 10)
            turtle.forward(movement)
            if turtle.pos()[0] >= 250:
                if userbet == turtle.color()[0]:
                    text = "Your bet was right!"
                else:
                    text = "sorry, your bet lost!"
                userbet = myscreen.textinput(title="Winner", prompt=text)
                race = False
                break

    myscreen.exitonclick()