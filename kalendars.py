import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()

def kalendars():
    def print_sel():
        print(cal.selection_get())
        if cal.selection_get():
            cursor.execute('INSERT INTO Atteiksana (Datums_no) VALUES (?)', (f"{cal.selection_get()}",))
            conn.commit()
            messagebox.showinfo("Veiksmīgi",'Datums pievienots!')
    
    top = tk.Toplevel(root)
    cal = Calendar(top,
                   font = 'Ariel 13' , selectnode= 'day',
                   cursor = 'hand1' , year = 2025 , month = 2 ,day = 5)
    cal.pack(fill = 'both', expand=True)
    ttk.Button(top , text = 'ok', command= print_sel).pack()



root = tk.Tk()
s = ttk.Style(root)
root.geometry('160x160+500+500')
s.theme_use('clam')
ttk.Button(root,text='Kalendārs',command=kalendars).pack(padx=10,pady=10)

root.mainloop()