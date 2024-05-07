from tkinter import *

# graphical user interface (tkinter module)
# we'll make a GUI which translates miles to km

window = Tk()
window.title("myfirst gui program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

# this uses advanced python arguments
my_label.pack(side="left") 

my_label['text'] = "new text"
my_label.config(text="newest text")

def button_clicked():
    my_label['text'] = input.get()

button = Button(text="butt text", command=button_clicked)
button.pack()

input = Entry(width=10)

input.pack()

# other interactive widgets:





#always at the bottom
window.mainloop()