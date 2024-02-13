from turtle import Turtle, Screen

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def ccw():
    tim.left(10)

def cw():
    tim.right(10)

def clearscreen():
    tim.clear()

if __name__ == "__main__":
    """
    W forward 10
    S backward 10
    A counter clockwise
    D clockwise
    C clear drawing
    """
    tim = Turtle()
    myscreen = Screen()
    myscreen.colormode(255)
    
    # get colors
    
    # turtle characteristics
    tim.speed(9)
    # method
    
    myscreen.listen()
    myscreen.onkey(key="w", fun=move_forwards)
    myscreen.onkey(key="s", fun=move_backwards)
    myscreen.onkey(key="a", fun=ccw)
    myscreen.onkey(key="d", fun=cw)
    myscreen.onkey(key="c", fun=clearscreen)

    myscreen.exitonclick()