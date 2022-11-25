import random
import time

rSzam = random.randint(1, 90)
lotto_on = True
talalat = 5

def lotto_game(num):
    global talalat
    global lotto_on
    if num < rSzam:
        print("A gondolt szám nagyobb")
        talalat = talalat - 1
    elif num > rSzam:
        print("A gondolt szám kissebb")
        talalat = talalat - 1
    else:
        print("Egy találatos szelvény")
        lotto_on = False


while lotto_on:
    szam = input("Találd ki a számot(1-90): ")
    if szam.isnumeric():

        szam1 = int(szam)

        if szam1 >= 1 and szam1 <= 90:
            lotto_game(szam1)
        else:
            print("1 és 90 között add meg a számot")

            talalat = talalat - 2
    else:
        print("Nem számot adtál meg")

        talalat = talalat - 2
    if talalat <= 0:
        print("0 találatos szelvény")
        lotto_on=False

time.sleep(50000)