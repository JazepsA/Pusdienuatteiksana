import sqlite3
from tkinter import *
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
                cursor.execute('INSERT INTO Atteiksana (Dat_no) VALUES (?)', (f"{cal.selection_get()}",))
                conn.commit()
                top.destroy()
                messagebox.showinfo("Veiksmīgi",'Datums pievienots!')
            
        
        top = tk.Toplevel(logs)
        cal = Calendar(top,
                    font = 'Ariel 13' , selectnode= 'day',
                    cursor = 'hand1' , year = 2025 , month = 2 ,day = 5)
        cal.pack(fill = 'both', expand=True)
        tk.Button(top , text = 'ok', command= print_sel).pack()


    def kalendars2():
        def print_sel():
            print(cal.selection_get())
            if cal.selection_get():
                cursor.execute('INSERT INTO Atteiksana (Dat_lidz) VALUES (?)', (f"{cal.selection_get()}",))
                conn.commit()
                top.destroy()
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
    logs.geometry("400x400")

    Lower_left=tk.Label(logs, text="id_skolnieka:")
    id_atteicejs_entry = tk.Entry(logs)
    id_atteicejs_entry.pack()
    id_atteicejs_entry.place(relx = 0.5 , rely = 0.1, anchor = CENTER)

    Lower_left.place(relx = 0.5 , rely = 0.05, anchor = CENTER)


    Lower_left1=tk.Label(logs, text="id_maksa:")
    id_maksa_entry = tk.Entry(logs)
    id_maksa_entry.pack()
    id_maksa_entry.place(relx = 0.5 , rely = 0.2, anchor = CENTER)

    Lower_left1.place(relx = 0.5 , rely = 0.15, anchor = CENTER)


    Lower_left2=tk.Label(logs, text="No:")
    Dat_no_entry = tk.Entry(logs)
    Dat_no_entry.pack()
    Dat_no_entry.place(relx = 0.5 , rely = 0.3, anchor = CENTER)


    Lower_left2.place(relx = 0.5 , rely = 0.25, anchor = CENTER)
        

    Lower_left3=tk.Label(logs, text="Līdz:")
    Dat_lidz_entry = tk.Entry(logs)
    Dat_lidz_entry.pack()
    Dat_lidz_entry.place(relx = 0.5 , rely = 0.4, anchor = CENTER)
    
    Lower_left3.place(relx = 0.5 , rely = 0.35, anchor = CENTER)
 


    
    
    kalendar= tk.Button(logs, text="", command=kalendars,overrelief="ridge",font=("Arial",11,"bold"))
    kalendar.pack(pady=10)
    kalendar.place(relx = 0.5 , rely = 0.3,x=80, anchor = CENTER)

    kalendar2= tk.Button(logs, text="", command=kalendars2,overrelief="ridge",font=("Arial",11,"bold"))
    kalendar2.pack(pady=10)
    kalendar2.place(relx = 0.5 , rely = 0.4,x=80, anchor = CENTER)


    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_pusdienu_att,overrelief="ridge",font=("Arial",11,"bold"))
    saglabat_btn.pack(pady=10)
    saglabat_btn.place(relx = 0.5 , rely = 0.5, anchor = CENTER)

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
    
    u=tk.Label(logs, text="Dienas:")
    dienas_entry = tk.Entry(logs)
    dienas_entry.pack()
    dienas_entry.place(relx = 0.5 , rely = 0.2, anchor = CENTER)

    u.place(relx = 0.5 , rely = 0.1, anchor = CENTER)

    uu=tk.Label(logs, text="Pusdienu cena:")
    pusdienu_cena_entry = tk.Entry(logs)
    pusdienu_cena_entry.pack()
    pusdienu_cena_entry.place(relx = 0.5 , rely = 0.4, anchor = CENTER)

    uu.place(relx = 0.5 , rely = 0.3, anchor = CENTER)

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=aprekinasana,overrelief="ridge",font=("Arial",11,"bold"))
    saglabat_btn.pack(pady=10)
    saglabat_btn.place(relx = 0.5 , rely = 0.55, anchor = CENTER)

#Funkcija , kas satur visas citas funkcijas.

def vecaku_logs():
    vecaki_logs = tk.Toplevel()
    vecaki_logs.title("Pusdienu atteikšanas pārvaldība")
    vecaki_logs.geometry(f"325x270+{int((vecaki_logs.winfo_screenwidth())/2)-162}+{int((vecaki_logs.winfo_screenheight())/2)-135}")

    pievienot_btn = tk.Button(vecaki_logs, text="Atteikt pusdienas", command=atteikt_pusdienas, width=25, height=2, bg="lightblue",font="bold",borderwidth=3)
    pievienot_btn.pack(pady=10)
    pievienot_btn.place(relx = 0.5 , rely = 0.2,y=20, anchor = CENTER)


    pievienot_btn1 = tk.Button(vecaki_logs, text="Aprēķināt pusdienu maksu", command=aprekinat_pusdienas, width=25, height=2, bg="lightgrey",font="bold",borderwidth=3)
    pievienot_btn1.pack(pady=10)
    pievienot_btn1.place(relx = 0.5 , rely = 0.4,y=20, anchor = CENTER)


    iziet_btn = tk.Button(vecaki_logs, text="Iziet", command=vecaki_logs.destroy, width=25, height=2, bg="red", fg="white",font="bold",borderwidth=3)
    iziet_btn.pack(pady=10)
    iziet_btn.place(relx = 0.5 , rely = 0.6,y=20, anchor = CENTER)
