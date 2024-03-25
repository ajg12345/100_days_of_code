#layout managers:
"""
pack things that are relative to one another
left 
right etc

place
place(x=100, y=100)
this is precise

grid
imagine and reference the row and column (0,0) is top left corner
and if there are 2 items, you can do a 1,2 or a 2,1 grid
!!can't mix grid and pack

"""
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1, column=1)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(row=2, column=3)

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(row=0, column=2)

window.mainloop()

