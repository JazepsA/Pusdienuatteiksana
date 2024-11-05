

import os 
import tkinter
from tkinter import *
from tkcalendar import Calendar
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x400")
 
# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = 2024, month = 11,
               day = 22)
 
cal.pack(pady = 20)
 

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
    print(cal.get_date())


# Add Button and Label

Button(root, text = "Get Date",command = grad_date).pack(pady = 20)




date = Label(root, text = "")


date.pack(pady = 20)
 
# Execute Tkinter
root.mainloop()

