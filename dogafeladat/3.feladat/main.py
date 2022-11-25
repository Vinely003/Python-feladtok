from kiiratas import Kiiratas

nev = input("Név: ")
a = input("A oldal: ")
b = input("B oldal: ")
c = input("C oldal: ")
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    sza = int(a)
    szb = int(b)
    szc = int(c)

    nyom=Kiiratas(nev,sza,szb,szc)
    nyom.nyomtatos_metodus()
else:
    print("Nem szám")
