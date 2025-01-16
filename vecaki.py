import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()

def atteikt_pusdienas():
    def saglabat_pusdienu_att():
        id_atteicejs = id_atteicejs_entry.get()
        id_maksa = id_maksa_entry.get()
        Dat_no = Dat_no_entry.get()
        Dat_lidz = Dat_lidz_entry.get()
        Dienas = Dienas_entry.get()

        if id_atteicejs and id_maksa and Dat_no and Dat_lidz and Dienas:
            cursor.execute(
                "INSERT INTO Atteiksana (id_atteicejs, id_maksa, Dat_no,Dat_lidz, Dienas) VALUES (?, ?, ?, ?, ?)",
                (id_atteicejs, id_maksa, Dat_no, Dat_lidz, Dienas)
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

    tk.Label(logs, text="Dienas:").pack()
    Dienas_entry = tk.Entry(logs)
    Dienas_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_pusdienu_att)
    saglabat_btn.pack(pady=10)


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

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=aprekinasana)
    saglabat_btn.pack(pady=10)

def vecaku_logs():
    vecaki_logs = tk.Toplevel()
    vecaki_logs.title("Pusdienu atteikšanas pārvaldība")
    vecaki_logs.geometry("300x250")

    pievienot_btn = tk.Button(vecaki_logs, text="Atteikt pusdienas", command=atteikt_pusdienas, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    pievienot_btn = tk.Button(vecaki_logs, text="Aprēķināt pusdienu maksu", command=aprekinat_pusdienas, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    iziet_btn = tk.Button(vecaki_logs, text="Iziet", command=vecaki_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)