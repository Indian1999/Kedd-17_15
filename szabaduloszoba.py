gameOn = True
rooms = []
items = []
chances = 3 # 3 lehetőségünk van kitalálni a kódot
solution = "4686"
switches = "0000000"
win = False

print("""Üdvözöllek a szabadulószobában! 14 ajtót látsz magad előtt, ezek közül
az egyik rejti a szabadságod kapuját! Találd ki a 4 számjegyű kódot, amivel
ki tudsz innen szabadulni! Sok sikert!""")
while gameOn:
    room_number = input("Melyik ajtón szeretnél bemenni? (0-13), (-1)\n")
    if room_number == "-1":
        print("A történeted eddig:")
        for i in range(len(rooms)):
            print(f"{rooms[i]}. szoba: {items[i]}")
    if room_number == "0":
        pass
    if room_number == "1":
        pass
    if room_number == "2":
        print("""Ebben a szobában a következő számsorozatot látod felírva egy tálbára: 1010011""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("1010011")
    if room_number == "3":
        print("""Ebben a szóbában egy videó van kivetítve a falra, amin egy cica eszik éppen a táljából
és a tálján azt látod, hogy egy 2-es számjegy szerepel.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Cica eszik a 2-es tálból")
    if room_number == "4":
        print("""Ebben a szobában egy tábla van tele villanykörtékkel, de nem világít mindegyik.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Tábla villanykörtékkel")
        if switches == "1010011":
            print("Olyan mintha egy 6-os számjegy rajzolódna ki a vilannykörtékből...")
            if "6-os villanykörték" not in items:
                rooms.append(room_number)
                items.append("6-os villanykörték")
    if room_number == "5":
        print("""Egy egyenlet van a falon: x = 10111 - 10001.
Biztos az x lesz az egyik számjegy...""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("x = 10111 - 10001")
    if room_number == "6":
        pass
    if room_number == "7":
        pass
    if room_number == "8":
        print("""A szobába belépve azt látod, hogy egy bohóc ül egy székben
és 3 színes lufit tart a kezében.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Bohóc 3 lufival")
    if room_number == "9":
        print("""Egy cetlit találasz a szobában, amire az van írva, hogy
binárisból decimálisa. Ez az info még biztos hasznos lesz...""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Cetli: binárisból decimálisba")
    if room_number == "10":
        print("""Ez az ajtó vezet a külvilághoz, add meg a 4 számjegyű kódot,
hogy kijuthass, de vigyázz, mert csak háromszor próbálkozhatsz!""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Kijárat")
        tipp = input("Szeretnél most próbálkozni? (igen/nem)\n")
        if tipp == "igen":
            code = input("Add meg a 4 számjegyet: ")
            if code == solution:
                gameOn = False
                win = True
            else:
                print("Helytelen kód!")
                chances -= 1
                print(f"Még {chances} próbálkozásod maradt.")
                if chances == 0:
                    gameOn = False
        else:
            print("Akkor majd legközelebb.")
    if room_number == "11":
        print("""A szobába belépve egy festményt találsz amin 2 bohóc látható ahogy egy cicát kergetnek.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("Festmény: 2 bohóc kerget egy cicát")
    if room_number == "12":
        print("""7 darab kapcsolót látsz a falon, de látszólag semmit nem csinálnak.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("7 kapcsoló a falon")
        switches = input("Add meg, hogy milyen sorrendben akarod felkapcsolni a kapcsolókat (pl.: 0101111)\n")
    if room_number == "13":
        pass

if win:
    print("Kijutottál! Szép volt!")
else:
    print("Ez most nem jött össze...")