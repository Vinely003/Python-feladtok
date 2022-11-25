def hathet():
    for i in range(10, 221):
        if i % 6 == 0 and i % 7 == 0:
            print("HatHét")
        elif i % 6 == 0:
            print("Hat")
        elif i % 7 == 0:
            print("Hét")
        else:
            print(i)

hathet()