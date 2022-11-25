from szamitas import Szamitas
import datetime

class Kiiratas:
    def __init__(self,nev,a,b):
        self.nev=nev
        self.a=a
        self.b=b

    def megkotberezlek(self):
        szamolas=Szamitas(self.a,self.b)
        szamolas.Kotber()

        datum=datetime.datetime.now().strftime("%Y.%m.%d")

        f=open("korosi_vince.txt","w")
        f.write("Kötbér kimutatás\n")
        f.write(f"Cég neve: {self.nev} \n")
        f.write(f"Projekt értéke: {self.a} Ft\n")
        f.write(f"Késedelmes napok száma: {self.b}\n")
        f.write(f"Kötbér összege: {szamolas.kotber} Ft\n")
        f.write(f"\nKelt: Szeged, {datum}")
        f.close()
    