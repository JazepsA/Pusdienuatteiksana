import sqlite3
import tkinter as tk
from tkinter import messagebox
from admin import skolnieku_logs

conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()


def izveidot_galveno_logu():
    def Administrators_poga():
        skolnieku_logs()

    def Vecaki_poga():
        treneru_logs()
    

    def apmeklejumi_poga():
        messagebox.showinfo("Apmeklējumi", "Atvērta apmeklējumu pārvaldība.")

    logs = tk.Tk()
    logs.title("Pusdienu atteiksana/samaksa")
    logs.geometry("300x200")

    sportisti_btn = tk.Button(logs, text="Administrators", command=Administrators_poga, width=20, height=2, bg="lightblue")
    sportisti_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Vecāki", command=Vecaki_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Apmeklējumi", command=apmeklejumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()