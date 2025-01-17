import sqlite3
import tkinter as tk
from tkinter import messagebox
from admin import skolnieku_logs
from vecaki import vecaku_logs
conn = sqlite3.connect('pusdienuatteiksana.db')
cursor = conn.cursor()


def izveidot_galveno_logu():
    def Administrators_poga():
        skolnieku_logs()

    def Vecaki_poga():
        vecaku_logs()
    


    logs = tk.Tk()
    logs.title("Pusdienu atteiksana/samaksa")
    logs.geometry(f"300x150+{int((logs.winfo_screenwidth())/2)-150}+{int((logs.winfo_screenheight())/2)-75}")


    sportisti_btn = tk.Button(logs, text="Administrators", command=Administrators_poga, width=20, height=2, bg="lightblue")
    sportisti_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Vecāki", command=Vecaki_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)


    logs.mainloop()





if __name__ == "__main__":
    izveidot_galveno_logu()