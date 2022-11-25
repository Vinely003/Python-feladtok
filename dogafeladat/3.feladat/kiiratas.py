from szamitas import Szamitas
import datetime

class Kiiratas:
    def __init__(self,nev,a,b,c):
        self.nev=nev
        self.a=a
        self.b=b
        self.c=c

    def nyomtatos_metodus(self):
        szamolas=Szamitas(self.a,self.b,self.c)
        szamolas.szamol()

        datum=datetime.datetime.now().strftime("%Y.%m.%d")

        f=open("korosi_vince.txt","w")
        f.write("Számításos lap")
        f.write(f"Felhasználó neve: {self.nev} \n")
        f.write(f"a oldal: {self.a} m\n")
        f.write(f"b oldal: {self.b} m\n")
        f.write(f"c oldal: {self.c} m\n")
        f.write(f"Kerület: {szamolas.kerulet} m\n")
        f.write(f"Terület: {szamolas.terulet} m2\n")
        f.write(f"\nKelt: Szeged, {datum}")
        f.close()
    