import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()

def pievienot_skolnieku():
    def saglabat_skolnieku():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()
        klase = klase_entry.get()
        telefons = telefons_entry.get()

        if vards and uzvards and telefons.isdigit() and klase.isdigit():
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

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_skolnieku)
    saglabat_btn.pack(pady=10)


def meklēt_skolnieku():
    def atrast_skolnieku():
        vards = vards_entry.get()
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

    logs = tk.Toplevel()
    logs.title("Meklēt skolnieku")
    logs.geometry("300x200")

    tk.Label(logs, text="Skolnieka vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_skolnieku)
    meklēt_btn.pack(pady=10)




def atjaunot_info():
    def atjauno_info():
        id_atteicejs =id_atteicejs_entry.get()
        if id_atteicejs:
            #cursor.execute("SELECT id_atteicejs, Vards,Uzvards,Klase,Maksa,Dienas FROM Atteicejs INNER JOIN Atteiksana on Atteicejs.id_atteicejs = Atteiksana.id_atteicejs INNER JOIN Maksa on Maksa.id_maksa = Atteiksana.id_maksa  WHERE id_atteicejs LIKE ? ", (f"%{id_atteicejs}%",))
            cursor.execute("SELECT Atteicejs.id_atteicejs,Vards,Uzvards,Klase,Tel_nr FROM Atteicejs INNER JOIN Atteiksana on Atteicejs.id_atteicejs = Atteiksana.id_atteicejs WHERE id_atteicejs LIKE ? ", (f"%{id_atteicejs}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}\n"

                    tk.Label(logs, text=f"Rezultāti\n ID:{r[0]} \n Vards: {r[1]}\n Uzvards: {r[2]}\n Klase: {r[3]}\n Maksas veids: {r[4]}\n").pack()


            else:
                messagebox.showinfo("Rezultāti", f"Netika atrasts neviens skolnieks ar id {id_atteicejs}.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet korektu skolnieka id!")

    logs = tk.Toplevel()
    logs.title("Rediģēt skolnieka informāciju")
    logs.geometry("300x200")

    tk.Label(logs, text="Skolnieka id:").pack()
    id_atteicejs_entry = tk.Entry(logs)
    id_atteicejs_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atjauno_info)
    meklēt_btn.pack(pady=10)

    #atveras_btn=tk.Button(logs,text="Informācija par skolnieku",command=atveras)
    #atveras_btn.pack(pady=10)



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

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_skolnieku_no_db)
    dzēst_btn.pack(pady=10)


def skolnieku_logs():
    skolnieki_logs = tk.Toplevel()
    skolnieki_logs.title("Skolnieku pārvaldība")
    skolnieki_logs.geometry(f"300x350+{int((skolnieki_logs.winfo_screenwidth())/2)-150}+{int((skolnieki_logs.winfo_screenheight())/2)-175}")

    pievienot_btn = tk.Button(skolnieki_logs, text="Pievienot skolnieku", command=pievienot_skolnieku, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(skolnieki_logs, text="Meklēt skolnieku", command=meklēt_skolnieku, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    meklēt_btn = tk.Button(skolnieki_logs, text="Rediģēt skolnieka info", command=atjaunot_info, width=25, height=2, bg="DarkGoldenrod1")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(skolnieki_logs, text="Dzēst skolnieku", command=dzēst_skolnieku, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(skolnieki_logs, text="Iziet", command=skolnieki_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)