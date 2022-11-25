import random
import time

rSzam = random.randint(101, 150)
jatekban_van = True
talalat = 5

def talalgatos_game(num):
    global talalat
    global jatekban_van
    if num < rSzam:
        print("A gondolt szám nagyobb")
        talalat = talalat - 1
    elif num > rSzam:
        print("A gondolt szám kissebb")
        talalat = talalat - 1
    else:
        print("Egy találatos szelvény")
        jatekban_van = False


while jatekban_van:
    szam = input("Találd ki a számot(101-150): ")
    if szam.isnumeric():

        szam1 = int(szam)

        if szam1 >= 101 and szam1 <= 150:
            talalgatos_game(szam1)
        else:
            print("101 és 150 között add meg a számot")

            talalat = talalat - 2
    else:
        print("Nem számot adtál meg")

        talalat = talalat - 2
    if talalat <= 0:
        print("0 találatos szelvény")
        jatekban_van=False

time.sleep(50000)