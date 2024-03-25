import tkinter

# graphical user interface (tkinter module)
# we'll make a GUI which translates miles to km

window = tkinter.Tk()
window.title("myfirst gui program")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() 
#always at the bottom
window.mainloop()