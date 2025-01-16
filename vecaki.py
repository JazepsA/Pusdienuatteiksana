import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()




def vecaku_logs():
    vecaki_logs = tk.Toplevel()
    vecaki_logs.title("Pusdienu atteikšanas pārvaldība")
    vecaki_logs.geometry("300x250")

    pievienot_btn = tk.Button(vecaki_logs, text="Atteikt pusdienas", command=atteikt_pusdienas, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(vecaki_logs, text="Meklēt t",command=meklēt_treneri, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(vecaki_logs, text="Dzēst treneri",command=dzēst_treneri, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(vecaki_logs, text="Iziet", command=vecaki_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)