import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from admin import skolnieku_logs
from vecaki import vecaku_logs
conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()






# Funkcija , kas izveido logu ,kuru lietotājs redzēs ieslēdzot to . 

def izveidot_galveno_logu():
    def Administrators_poga():
        skolnieku_logs()

    def Vecaki_poga():
        vecaku_logs()


    logs = tk.Tk()
    logs.title("Pusdienu atteiksana/samaksa")
    logs.geometry(f"325x270+{int((logs.winfo_screenwidth())/2)-162}+{int((logs.winfo_screenheight())/2)-135}")
    logs.configure(bg="lightgrey")




    sportisti_btn = tk.Button(logs, text="Administrators", command=Administrators_poga, width=20, height=2, bg="lightblue",font=("Bookman Old Style",14,"bold"),bd=5,activebackground="White")
    sportisti_btn.pack(pady=10)
    sportisti_btn.place(relx = 0.5 , rely = 0.2, anchor = CENTER)

    treneri_btn = tk.Button(logs, text="Vecāki", command=Vecaki_poga, width=20, height=2, bg="lightgreen",font=("Bookman Old Style",14,"bold"),bd=5,activebackground="White")
    treneri_btn.pack(pady=10)
    treneri_btn.place(relx = 0.5 , rely = 0.5, anchor = CENTER)

    iziet_btn = tk.Button(logs, text="Iziet", command=logs.destroy, width=20, height=2, bg="red", font=("Bookman Old Style",14,"bold"),bd=5,activebackground="White")
    iziet_btn.pack(pady=10)
    iziet_btn.place(relx = 0.5 , rely = 0.8, anchor = CENTER)


    logs.mainloop()





if __name__ == "__main__":
    izveidot_galveno_logu()