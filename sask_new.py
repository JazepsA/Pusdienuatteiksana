import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from admin_new import skolnieku_logs
from vecaki import vecaku_logs
import re
conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()






# Funkcija , kas izveido logu ,kuru lietotājs redzēs ieslēdzot to . 

def izveidot_galveno_logu():
    def Administrators_poga():
        def parolee():
            parole = parolew.get()

            pattern= r'^Adazi123$'
            if not re.match(pattern, parole):
                messagebox.showerror("Rezultāts", "Nepareizi ievadīta parole!")
            else:
            
                skolnieku_logs()

        Administrators_poga = tk.Toplevel()
        Administrators_poga.title("Parole")
        Administrators_poga.geometry(f"300x370+{int((Administrators_poga.winfo_screenwidth())/2)-150}+{int((Administrators_poga.winfo_screenheight())/2)-185}")

        tk.Label(Administrators_poga, text="Ievadiet paroli:").pack()
        parolew = tk.Entry(Administrators_poga)
        parolew.pack()

        knopka = tk.Button(Administrators_poga, text="Ienākt", command=parolee,overrelief="ridge",font=("Arial",11,"bold"))
        knopka.pack(pady=10)

    def Vecaki_poga():
        vecaku_logs()


    logs = tk.Tk()
    logs.title("Galvenais logs")
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