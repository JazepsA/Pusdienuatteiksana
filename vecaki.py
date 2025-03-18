import sqlite3
import tkinter as tk
from tkinter import messagebox
import sys
from datetime import datetime
import re
from tkcalendar import Calendar

#from kalendars import kalendars



conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()


#Funkcija , kas ļauj atteikt pusdienas ,izveidot pusdienu atteikšanu.

def atteikt_pusdienas():
    
    def kalendars():
        def print_sel():
            print(cal.selection_get())
            if cal.selection_get():
                cursor.execute('INSERT INTO Atteiksana (Datums_no) VALUES (?)', (f"{cal.selection_get()}",))
                conn.commit()
                messagebox.showinfo("Veiksmīgi",'Datums pievienots!')
        
        top = tk.Toplevel(logs)
        cal = Calendar(top,
                    font = 'Ariel 13' , selectnode= 'day',
                    cursor = 'hand1' , year = 2025 , month = 2 ,day = 5)
        cal.pack(fill = 'both', expand=True)
        tk.Button(top , text = 'ok', command= print_sel).pack()



    def saglabat_pusdienu_att():
        id_atteicejs = id_atteicejs_entry.get()
        id_maksa = id_maksa_entry.get()
        Dat_no = Dat_no_entry.get()
        Dat_lidz = Dat_lidz_entry.get()


        pattern = r'\d+$'
    
        if not re.match(pattern, id_atteicejs):
            messagebox.showerror("Rezultāts", "Vards nav derīga!")

        if id_atteicejs and id_maksa and Dat_no and Dat_lidz:

            try:
                Pirmais = datetime.strptime(Dat_no, '%d-%m-%Y')
                Otrais = datetime.strptime(Dat_lidz, '%d-%m-%Y')
                starp=Otrais - Pirmais
            except ValueError:
                tk.Label(logs, text="Nepariezi ievadīts datums!")

            


            

            cursor.execute(
                "INSERT INTO Atteiksana (id_atteicejs, id_maksa, Dat_no,Dat_lidz,Dienas) VALUES (?, ?, ?, ?,?)",
                (id_atteicejs, id_maksa, Dat_no, Dat_lidz,str(starp))
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Pusdienas ir veiksmīgi atteiktas!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Atteikt pusdienas")
    logs.geometry("300x300")

    tk.Label(logs, text="id_skolnieka:").pack()
    id_atteicejs_entry = tk.Entry(logs)
    id_atteicejs_entry.pack()

    tk.Label(logs, text="id_maksa:").pack()
    id_maksa_entry = tk.Entry(logs)
    id_maksa_entry.pack()

    tk.Label(logs, text="No:").pack()
    Dat_no_entry = tk.Entry(logs)
    Dat_no_entry.pack() 
        

    tk.Label(logs, text="Līdz:").pack()
    Dat_lidz_entry = tk.Entry(logs)
    Dat_lidz_entry.pack()


    
    
    kalendar= tk.Button(logs, text="", command=kalendars,overrelief="ridge",font=("Arial",11,"bold"))
    kalendar.pack(pady=10)
    kalendar.place(x=200,y=100)

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_pusdienu_att,overrelief="ridge",font=("Arial",11,"bold"))
    saglabat_btn.pack(pady=10)

#Funkcija ar kuras palīdzību var aprēķināt pusdienu summu.

def aprekinat_pusdienas():
    def aprekinasana():
        dienas=dienas_entry.get()
        pusdienu_cena=pusdienu_cena_entry.get()

        if dienas and pusdienu_cena:
            a=int(dienas) * float(pusdienu_cena)
            tk.Label(logs, text=f"Gala cena: {a}").pack()



    logs = tk.Toplevel()
    logs.title("Aprēķināt pusdienu cenu")
    logs.geometry("300x300")
    
    tk.Label(logs, text="Dienas:").pack()
    dienas_entry = tk.Entry(logs)
    dienas_entry.pack()

    tk.Label(logs, text="Pusdienu cena:").pack()
    pusdienu_cena_entry = tk.Entry(logs)
    pusdienu_cena_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=aprekinasana,overrelief="ridge",font=("Arial",11,"bold"))
    saglabat_btn.pack(pady=10)

#Funkcija , kas satur visas citas funkcijas.

def vecaku_logs():
    vecaki_logs = tk.Toplevel()
    vecaki_logs.title("Pusdienu atteikšanas pārvaldība")
    vecaki_logs.geometry(f"300x220+{int((vecaki_logs.winfo_screenwidth())/2)-150}+{int((vecaki_logs.winfo_screenheight())/2)-110}")

    pievienot_btn = tk.Button(vecaki_logs, text="Atteikt pusdienas", command=atteikt_pusdienas, width=25, height=2, bg="lightblue",font="bold",borderwidth=3)
    pievienot_btn.pack(pady=10)


    pievienot_btn = tk.Button(vecaki_logs, text="Aprēķināt pusdienu maksu", command=aprekinat_pusdienas, width=25, height=2, bg="lightgrey",font="bold",borderwidth=3)
    pievienot_btn.pack(pady=10)

    iziet_btn = tk.Button(vecaki_logs, text="Iziet", command=vecaki_logs.destroy, width=25, height=2, bg="red", fg="white",font="bold",borderwidth=3)
    iziet_btn.pack(pady=10)
