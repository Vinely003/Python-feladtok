from kiiratas import Kiiratas

nev = input("Név: ")
a = input("Szam1: ")
b = input("Szam2: ")
if a.isnumeric() and b.isnumeric():
    sza = int(a)
    szb = int(b)

    nyom=Kiiratas(nev,sza,szb)
    nyom.megkotberezlek()
else:
    print("Nem szám")
