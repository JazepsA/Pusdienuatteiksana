import sqlite3
import tkinter as tk
from tkinter import messagebox,ttk
from tkinter import ttk
import re

conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()


#Funkcija , kas ļauj pievienot jaunus skolniekus.

def pievienot_skolnieku():
    def saglabat_skolnieku():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()
        klase = klase_entry.get()
        telefons = telefons_entry.get()

        pattern= r'^[A-ZĀ-Ž][a-zā-ž]+$|^[A-ZĀ-Ž][a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'
        if not re.match(pattern, vards):
            messagebox.showerror("Rezultāts", "Nepareizi ievadīts vārds!")

        pattern2= r'^[A-ZĀ-Ž][a-zā-ž]+$|^[A-ZĀ-Ž][a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'
        if not re.match(pattern2, uzvards):
            messagebox.showerror("Rezultāts", "Nepareizi ievadīts uzvārds!")

        pattern3= r'\d{1,2}+$|\d[1-9]{1}.[a-z]+$|[1]{1}[012]{2}.[123]{1}+$'
        if not re.match(pattern3, klase):
            messagebox.showerror("Rezultāts", "Nepareizi ievadīta klase!")

        pattern4= r'\d{8}'
        if not re.match(pattern4, telefons):
            messagebox.showerror("Rezultāts", "Nepareizi ievadīts telefona numurs!(Rakstiet numuru bez trīsciparu koda!)")


        if vards and uzvards and telefons and klase:
            cursor.execute(
                "INSERT INTO Atteicejs (Vards,Uzvards,Klase,Tel_nr) VALUES (?, ?, ?, ?)",
                (vards, uzvards, int(klase), int(telefons))
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Skolnieks pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot skolnieku")
    logs.geometry("300x300")

    tk.Label(logs, text="Vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Klase:").pack()
    klase_entry = tk.Entry(logs)
    klase_entry.pack()

    tk.Label(logs, text="Telefona numurs:").pack()
    telefons_entry = tk.Entry(logs)
    telefons_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_skolnieku,overrelief="ridge",font=("Arial",11,"bold"))
    saglabat_btn.pack(pady=10)

#Funkcija , kas ļauj atrast skolnieku.

def meklēt_skolnieku():
    def atrast_skolnieku():
        id = vards_entry.get()
        
        patternn= r'\d'
        if not re.match(patternn, id):
            messagebox.showerror("Kļūda", "Nepareizi ievadīts id!")
            
        '''
        if vards:
            cursor.execute("SELECT * FROM Atteicejs WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}\n"
                    messagebox.showinfo("Rezultāti", f"ID:{r[0]}  Vards: {r[1]} Uzvards: {r[2]}, Klase: {r[3]}, Telefona numurs: {r[4]}\n")
            else:
                messagebox.showinfo("Rezultāti", f"Netika atrasts neviens skolnieks/ce ar vārdu {vards}.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet skolnieka vārdu!")
            '''
        
        if id:
                cursor.execute("SELECT * FROM Atteicejs WHERE id_atteicejs LIKE ?", (f"%{id}%",))
                rezultati = cursor.fetchall()
                if rezultati:
                    rezultati_str = ""
                    for r in rezultati:
                        rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}\n"
                        messagebox.showinfo("Rezultāti", f"ID:{r[0]}  Vārds: {r[1]} Uzvārds: {r[2]} Klase: {r[3]} Telefona numurs: {r[4]}\n")
                else:
                    messagebox.showinfo("Rezultāti", f"Netika atrasts neviens skolnieks/ce ar id {id}.")
        else:
                messagebox.showerror("Kļūda", "Lūdzu, ievadiet korektu id !")


    logs = tk.Toplevel()
    logs.title("Meklēt skolnieku")
    logs.geometry("300x200")

    tk.Label(logs, text="Skolnieka id:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_skolnieku,overrelief="ridge",font=("Arial",11,"bold"))
    meklēt_btn.pack(pady=10)


#Funkcija , kas ļauj atjaunot informāciju par skolnieku.

def atjaunot_info():
    def atjauno_info():
        id_atteicejs =id_atteicejs_entry.get()
        if id_atteicejs:
            cursor.execute("SELECT Vards,Uzvards,Klase , Maksa.Maksa FROM Atteicejs INNER JOIN Atteiksana ON Atteicejs.id_atteicejs= Atteiksana.id_atteicejs INNER JOIN Maksa ON Atteiksana.id_maksa= Maksa.id_maksa WHERE Atteicejs.id_atteicejs LIKE ? ", (f"%{id_atteicejs}%",) )    
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"

                    tk.Label(logs, text=f"Rezultāti\n Vārds:{r[0]} \n Uzvārds: {r[1]}\n Klase: {r[2]}\n Maksas veids:{r[3]}\n").pack()


            else:
                messagebox.showinfo("Rezultāti", f"Netika atrasts neviens skolnieks ar id {id_atteicejs}.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet korektu skolnieka id!")

        ttk.Label(logs, text = "Izvēlieties ,ko vēlaties pamainīt: ",  font = ("Times New Roman", 10)).grid(column = 0, row = 15, padx = 10, pady = 25) 
            
        n = tk.StringVar() 
        monthchoosen = ttk.Combobox(logs, width = 27,textvariable = n) 
            
            
        monthchoosen['values'] = (' January',  
                                    ' February', 
                                    ' March', 
                                    ' April', 
                                    ' May', 
                                    ' June',  
                                    ' July',  
                                    ' August',  
                                    ' September',  
                                    ' October',  
                                    ' November',  
                                    ' December') 
            
        monthchoosen.grid(column = 1, row = 15) 




    logs = tk.Toplevel()
    logs.title("Rediģēt skolnieka informāciju")
    logs.geometry("300x200")

    tk.Label(logs, text="Skolnieka id:").pack()
    id_atteicejs_entry = tk.Entry(logs)
    id_atteicejs_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atjauno_info,overrelief="ridge",font=("Arial",11,"bold"))
    meklēt_btn.pack(pady=10)

    #atveras_btn=tk.Button(logs,text="Informācija par skolnieku",command=atveras)
    #atveras_btn.pack(pady=10)

#Funkcija , kas ļauj idzēst skolnieku no datu bāzes.

def dzēst_skolnieku():
    def dzēst_skolnieku_no_db():
        id_skolnieka = id_skolnieka_entry.get()
        if id_skolnieka.isdigit():
            cursor.execute("DELETE FROM Atteicejs WHERE id_atteicejs = ?", (id_skolnieka))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Sportists ar ID {id_skolnieka} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst skolnieku")
    logs.geometry("300x150")

    tk.Label(logs, text="Skolnieka ID:").pack()
    id_skolnieka_entry = tk.Entry(logs)
    id_skolnieka_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_skolnieku_no_db,overrelief="ridge",font=("Arial",11,"bold"))
    dzēst_btn.pack(pady=10)

#Funkcija , kas satur visas citas funkcijas .

def skolnieku_logs():
    skolnieki_logs = tk.Toplevel()
    skolnieki_logs.title("Skolnieku pārvaldība")
    skolnieki_logs.geometry(f"300x370+{int((skolnieki_logs.winfo_screenwidth())/2)-150}+{int((skolnieki_logs.winfo_screenheight())/2)-185}")

    pievienot_btn = tk.Button(skolnieki_logs, text="Pievienot skolnieku", command=pievienot_skolnieku, width=25, height=2, bg="lightblue",font="bold",borderwidth=3)
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(skolnieki_logs, text="Meklēt skolnieku", command=meklēt_skolnieku, width=25, height=2, bg="lightgreen",font="bold",borderwidth=3)
    meklēt_btn.pack(pady=10)

    meklēt_btn = tk.Button(skolnieki_logs, text="Rediģēt skolnieka info", command=atjaunot_info, width=25, height=2, bg="DarkGoldenrod1",font="bold",borderwidth=3)
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(skolnieki_logs, text="Dzēst skolnieku", command=dzēst_skolnieku, width=25, height=2, bg="lightyellow",font="bold",borderwidth=3)
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(skolnieki_logs, text="Iziet", command=skolnieki_logs.destroy, width=25, height=2, bg="red", fg="white",font="bold",borderwidth=3)
    iziet_btn.pack(pady=10)