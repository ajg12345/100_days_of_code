"""
the layout must be:
            |0          |miles
 is equal to|0          |km
            |Calculate  |

"""
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

#Labels
calc_label = Label(text="is equal to")
calc_label.grid(row=1, column=0)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

km_value = Label(text=0)
km_value.grid(row=1, column=1)

#Buttons
def calculat_km():
    km_value['text'] = int(miles_entry.get()) * 1.60934

#calls action() when pressed
button = Button(text="Calculate", command=calculat_km)
button.grid(row=2, column=1)

#Entries
miles_entry = Entry(width=30)
#Add some text to begin with
miles_entry.insert(END, string="input miles integer")
#Gets text in entry
miles_entry.grid(row=0, column=1)


window.mainloop()

