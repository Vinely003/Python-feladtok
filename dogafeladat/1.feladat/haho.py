def haho():
    for i in range(10, 221):
        if i % 5 == 0 and i % 11 == 0:
            print("Hahó")
        elif i % 5 == 0:
            print("Ha")
        elif i % 11 == 0:
            print("Hó")
        else:
            print(i)

haho()