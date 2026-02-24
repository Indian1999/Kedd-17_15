money = int(input("Pénz: "))

cimletek = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]

for cimlet in cimletek:
    print(f"{money // cimlet} db {cimlet} Ft-os")
    money %= cimlet