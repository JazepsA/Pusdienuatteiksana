import itertools
import datetime
import json
from datetime import date
import sqlite3 as db

with db.connect('pusdienuatteiksana.db') as con:
    cur=con.cursor()
    vards=int(input("Ievadiet savu vardu:"))
    uzvards=input("Ievadiet savu uzvardu:")
    klase=float(input("Ievadiet savu klasi:"))
    tel_nr=input("Ievadiet savu telefona numuru: ")

    cur.execute(''' INSERT INTO Atteicejs(produkta_id,nosaukums,cena,noliktava) VALUES (?,?,?,?) ''',(produkta_id,nosaukums,cena,noliktava))







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




try:
    with open("people_data.json","r",encoding="utf-8") as file:
        people=json.load(file)


except FileExistsError:
    people=[]

 
while True:
    print("Labdien!")
    a=input("Vai velaties atteikt pusdienas(jā/nē):  ")
    if a == "jā":
        vards=input("Ievadiet vārdu: ")
        uzvards=input("Ievadiet savu uzvārdu")
        klase=input("Ievadiet klasi ,kurā jūs mācaties: ")
        tel_nr=input("Ievadiet savu tel_nr: ")



    people.append({
        "vards":vards,
        "klase":klase,
        "tel_nr":tel_nr
        "pusdienuatteiksana":[]
    })


    while True:
        another=input("Vai vēlaties atteikt pusdienas (jā/nē)").strip().lower()
        if another =="jā":
            print("Atteikt pusdienas")
            dat_no=input("Ievadiet datumu no kura jus velaties atteikt pusdienas: ")
            dat_lidz=input("Ievadiet datumu lidz kuram jus velaties atteikt pusdienas: ")

            pusdienuatteiksana.append({
            "dat_no":dat_no,
            "dat_lidz":dat_lidz,
        })


            a=Atteikt("12.10.2024","14.10.2024","1.5")
            print(a)

        else:
            print("Paldies par izmantošanu!")
            break
    break


with open("people_data.json","w",encoding="utf-8") as file:
    json.dump(people,file,indent=4)


print("Dati ir veiksmīgi saglabāti JSON failā! ")




att1=Atteikt(name,age,city)





'''

def main():
    load_data()
    find_organisation_by_id()
    count_organisations()
    list_organisation_ids()
    organisation_exists()
    delete_organisation_by_id()
    while (True):
        response=input("(1) Add organisation (2) Print organisations (3) Exit ")
        if response=="1":
            add_organisation()
        elif response =="2":
            print_organisation()
        elif response =="3":
            save_data()
            print("Bye bye!")
            exit()
        else:
            print("Choose a number between 1 and 3")
            continue
main()

'''