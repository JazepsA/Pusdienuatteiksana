import itertools
import datetime
from datetime import date
import sqlite3 as db
import sqlite3

#conn=sqlite3.connect("pusdienuatteiksana.db")
#cur=conn.cursor()

class Funkcijas():

    def pievienot():
        with db.connect('pusdienuatteiksana.db') as con:
            cur=con.cursor()
            id_atteicejs=int(input("Ievadiet atteiceja id: "))
            vards=input("Ievadiet savu vardu:")
            uzvards=input("Ievadiet savu uzvardu:")
            klase=input("Ievadiet savu klasi:")
            tel_nr=int(input("Ievadiet savu telefona numuru: "))
            cur.execute(''' INSERT INTO Atteicejs(id_atteicejs,Vards,Uzvards,Klase,Tel_nr) VALUES (?,?,?,?,?) ''',(id_atteicejs,vards,uzvards,klase,tel_nr))
            con.commit()
    
    def Izvada():
        with db.connect('pusdienuatteiksana.db') as con:
            cur=con.cursor()
            cur.execute("SELECT * FROM Atteicejs" )
            order=cur.fetchall()
            for i in order:
                print(i)

    def dzest():
        with db.connect('pusdienuatteiksana.db') as con:
            cur=con.cursor()
            while True:
                gone=int(input("Ievadiet id ,kuru velaties izdzest (ja uzrakstita id nav tad rakstiet velreiz,ja pardomajat dzest ara ,tad raksties '0')"))
                if gone != 0 :
                    con.execute(f"DELETE FROM Atteicejs WHERE id_atteicejs = {gone}")
                    print("Dati tika dzesti!")
                    con.commit()
                    print(cur.rowcount,"Izdzests")

                elif gone == 0:
                    print("Jus atsutija atpakaļ!")
                    break
                else:
                    pass
    def atrast():
        with db.connect('pusdienuatteiksana.db') as con:
                    cur=con.cursor()
                    while True:
                        atrast=int(input("Ievadiet id ,kuru velaties atrast(ja uzrakstita id nav tad rakstiet velreiz,ja pardomajat,tad raksties '0')"))
                        if atrast != 0 :
                            print(f"Persona ar {atrast} id tika atrasta  !")
                            con.execute(f"SELECT * FROM Atteicejs WHERE id_atteicejs = {atrast}")
                            con.commit()
                            info=cur.fetchall()
                            print(info)
                            for rinda in info:
                                print(rinda)
            
                            

                        elif atrast == 0:
                            print("Jus atsutija atpakaļ!")
                            break
                        else:
                            pass





        
        

class Atteikt:
    atteiksanasDatumsNo= ""
    atteiksanasDatumsLidz=""
    pusdienuMaksaVienaDiena = 0

    id_iter= itertools.count()

    def __init__(self,dat_no,dat_lidz,pus_mak_diena=1.5):
        self.atteiksanasId=next(self.id_iter)+1
        self.atteiksanasDatumsNo=dat_no
        self.atteiksanasDatumsLidz=dat_lidz
        self.pusdienuMaksaVienaDiena=pus_mak_diena


    def Atteiksanas_info(self):
        return [
            self.atteiksanasDatumsNo,self.atteiksanasDatumsLidz,
            self.pusdienuMaksaVienaDiena
        ]

    def Atteiksanas_info_print(self):
        print("Pusdienu atteikšanas datums no: "+ str(self.atteiksanasDatumsNo))
        print("Pusdienu atteikšanas datums līdz: " + str(self.atteiksanasDatumsLidz))
        print("Pusdienu maksa vienā dienā: "+ str(self.pusdienuMaksaVienaDiena))

class Atteicejs:
    vards=""
    uzvards=""
    personasKods=""

    id_iter= itertools.count()

    def __init__(self,vards,uzv,per_kods):
        self.atteiksanasId=next(self.id_iter)+1
        self.vards=vards
        self.uzvards=uzv
        self.personasKods=per_kods

    def Atteiceja_info(self):
        return [
            self.vards,self.uzvards,
            self.personasKods
        ]


    def Atteiceja_info_print(self):
        print("Atteiceja vards: "+ str(self.vards))
        print("Atteiceja uzvārds: " + str(self.uzvards))
        print("Atteiceja personas kods : "+ str(self.personasKods))





def main():
    while (True):
        response=input("(1) Pievienot jaunu cilveku(2) Izvadit informaciju (3)Izdzest personu (4)atrast atteiceju un atteikt pusd. (7) Exit ")
        if response=="1":
            Funkcijas.pievienot()
        elif response =="2":
            Funkcijas.Izvada()
        elif response =="3":
            Funkcijas.dzest()
        elif response == "4":
            Funkcijas.atrast()
        elif response =="7":
            print("Bye bye!")
            exit()
        else:
            print("Choose a number between 1 and 3")
            continue
main()





att1=Atteikt("2024.09.12","2024.09.16",1.5)
att2=Atteikt("2024.10.16","2024.10.20",2)
att3=Atteikt("2024.12.03","2024.12.07",1)

atteicejs1=Atteicejs("Nikita","Arbuzov","430921-12314")
atteicejs2=Atteicejs("Dainis","Bernans","130915-64314")
atteicejs3=Atteicejs("Hubs","Diks","111021-79314")

print(att1.atteiksanasId)
att1.Atteiksanas_info()
att1.Atteiksanas_info_print()
print(att2.atteiksanasId)
att2.Atteiksanas_info()
att2.Atteiksanas_info_print()
print(att3.atteiksanasId)
att3.Atteiksanas_info()
att3.Atteiksanas_info_print()
print(atteicejs1.atteiksanasId)
atteicejs1.Atteiceja_info()
atteicejs1.Atteiceja_info_print()
print(atteicejs2.atteiksanasId)
atteicejs2.Atteiceja_info()
atteicejs2.Atteiceja_info_print()
print(atteicejs3.atteiksanasId)
atteicejs3.Atteiceja_info()
atteicejs3.Atteiceja_info_print()


    
