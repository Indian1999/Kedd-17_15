import os

path = os.path.join(os.path.dirname(__file__), "kerekpar-adatok.txt")

boltok = []

with open(path, encoding="utf-8") as f:
    next(f) # Átugorja az első sort
    for line in f: 
        # Bicikli Pont;Budapest;4500
        line = line.strip().split(";") # ['Kerék Expressz', 'Budapest', '5500']
        bolt = {
            "name": line[0],
            "city": line[1],
            "price": int(line[2])
        }
        boltok.append(bolt)
        
#1. Írd ki, hogy hány kerékpárbolt van összesen!
print(f"Összesen {len(boltok)} kerékpárbolt szerepel az adatok között.")

#2. Írd ki, hogy melyik boltban a legdrágább egy kerékpár szervizelése és mennyibe
#kerül!

max_index = 0
for i in range(1, len(boltok)):
    if boltok[i]["price"] > boltok[max_index]["price"]:
        max_index = i

print(f"{boltok[max_index]['name']} a legdrágább üzlet, egy szervíz {boltok[max_index]['price']} Ft-ba kerül.")

#3.  Írj  egy  függvényt  akcio  néven,  ami  paraméterként  megkapja  a  szerviz  árát  és
#visszaadja, hogy mennyibe kerülne 20%-os kedvezménnyel!

def akcio(ar):
    return ar * 0.8

#4. Kérj be a felhasználótól egy bolt nevet, majd írd ki, hogy az adott boltban mennyi
#lenne  a  szerviz  ár  20%-os  kedvezménnyel!  (az  előző  feladatban  lévő  függvényt
#használd fel hozzá) Ha nincs ilyen nevű bolt, akkor írd ki, hogy nincs ilyen bolt!

bolt = input("Add meg egy bolt nevét: ")

talalat = False
for item in boltok:
    if item["name"] == bolt:
        talalat = True
        print(f"Ebben a boltban, 20 %-os kedvezménnyel {akcio(item['price'])} Ft-ba kerülne.")
        break

if not talalat:
    print("Nincs ilyen nevű bolt!")

#5. Írd ki a kerekpar-export.txt fájlba a Budapesti boltok neveit!

path = os.path.join(os.path.dirname(__file__), "kerekpar-export.txt")

with open(path, "w", encoding="utf-8") as f:
    for item in boltok:
        if item["city"] == "Budapest":
            f.write(item["name"])
            f.write("\n")



