import os

szerverek = []
path = os.path.join(os.path.dirname(__file__), "minecraft-adatok.txt")

with open(path, encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip().split(";")
        szerver = {
            "name": line[0],
            "mode": line[1],
            "players": int(line[2]),
            "price": int(line[3])
        }
        szerverek.append(szerver)


#1. Írd ki, hogy hány szerver van összesen!
print(f"Összesen {len(szerverek)} db szerver szerepel az adatok között.")

#2. Írd ki, hogy melyik szerveren van a legtöbb játékos és hány fő!

max_index = 0
for i in range(1, len(szerverek)):
    if szerverek[i]["players"] > szerverek[max_index]["players"]:
        max_index = i

print(f"{szerverek[max_index]['name']} szerveren van a legtöbb játékos ({szerverek[max_index]['players']}).")

#3.  Írj  egy  függvényt  vip_ar  néven,  ami  paraméterként  megkapja  a  havi  díjat  és
#visszaadja, hogy mennyibe kerülne a VIP csomag, ami 50%-kal drágább!

def vip_ar(ar):
    return ar * 1.5

#4.  Kérj  be  a  felhasználótól  egy  szerver  nevet,  majd  írd  ki,  hogy  az  adott  szerveren
#mennyi  lenne  a  VIP  csomag  ára!  (az  előző  feladatban  lévő  függvényt  használd  fel
#hozzá) Ha nincs ilyen nevű szerver, akkor írd ki, hogy nincs ilyen szerver!

szerver = input("Add meg egy szerver nevét: ")

talalat = False
for item in szerverek:
    if item["name"] == szerver:
        talalat = True
        print(f"Ezen a szerveren a VIP tagság {vip_ar(item['price'])} Ft-ba kerül.")
        break

if not talalat:
    print("Nincs ilyen nevű szerver!")

#5. Írd ki a minecraft-export.txt fájlba a survival módú szerverek neveit!

path = os.path.join(os.path.dirname(__file__), "minecraft-export.txt")

with open(path, "w", encoding="utf-8") as f:
    for szerver in szerverek:
        if szerver["mode"] == "survival":
            f.write(szerver["name"] + "\n")