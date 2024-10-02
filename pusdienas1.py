import itertools
import datetime
from datetime import date

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


    
