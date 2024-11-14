import itertools
import os
import tkinter as tk
import datetime
from datetime import date


def open_calendar():
    os.system('kalendars.py')




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
        self.atteiksanasId=next(self.id_iter)
        self.vards=vards
        self.uzvards=uzv
        self.personasKods=per_kods

    def Atteiceja_info(self):
        return [
            self.vards,self.uzvards,
            self.personasKods
        ]


    def Atteiceja_info_print(self):
        print("Kartas Nr."+str(self.atteiksanasId))
        print("Atteiceja vards: "+ str(self.vards))
        print("Atteiceja uzvārds: " + str(self.uzvards))
        print("Atteiceja personas kods : "+ str(self.personasKods))


btn=tk.Button(text="Calendars",command=open_calendar)



with open("atteicejuInfo.txt","a",encoding="utf-8") as fail:

    while True:
        atteicejsInfo=[]

        velReiz=input("Vai gribat ievadit vēl vienu personu? : jā/nē ?")
        if velReiz == "jā":

            cilvekaVards= input("Ievadiet savu vārdu: ")
            cilvekaUzvards= input("Ievadiet savu uzvārdu: ")
            cilvekaPersonasKods=input("Ievadiet savu personas kodu: ")
            print(cilvekaVards)
            atteicejs1=Atteicejs("Nikita","Arbuzov","430921-12314")
            atteicejsInfo.append(atteicejs1) 
        
            atteicejs2=Atteicejs(cilvekaVards,cilvekaUzvards,cilvekaPersonasKods)
            print(atteicejs2)

            atteicejsInfo.append(atteicejs2) 
            print(atteicejsInfo)

            print(atteicejs2.atteiksanasId) 
            atteicejs2.Atteiceja_info()
            atteicejs2.Atteiceja_info_print()

            fail.writelines(f"Cilveka vards{cilvekaVards},uzvards {cilvekaUzvards},personas kods {cilvekaPersonasKods} \n")


        elif velReiz == "nē":
            print("Paldies par uzmanību!")
            break







#datumsNo= input("Ievadiet datumu no kura atteikt pusdienas: ")
#datumsLidz= input("Ievadiet datumu līdz kuram atteikt pusdienas: ")



'''


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

'''