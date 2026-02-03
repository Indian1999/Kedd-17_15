import os 
import random
# A dictionary (szótár) adatszerkezet

"""
szotar = {} # Egy üres dictionaryt hoz létre
szotar = {
    "alma": "apple",
    "ananász": "pineapple",
    "bögre": "mug",
    "citrom": "lemon",
    "citrom": "citrus", # lemon-ról átíródik citrusra
    "kukorica": "corn",
    "kirabolni": "mug"
}

print(szotar)
print(type(szotar)) # <class 'dict'>
print(len(szotar)) # 5
print(szotar["bögre"]) # mug
print(szotar["citrom"]) # citrus

# A dictionary kulcs-érték párokat tárol
# Egy kulcs csak egyszer szerepelhet a szótárban!
# Az értékekre nincs ilyen megkötés

#########################
# Dictionary-k bejárása #
#########################

def opcio1(dict):
    for item in dict.keys():
        #print(item) # ananász, alma, bögre, .... (A dictionary kulcsain megy végig)
        #print(type(item)) # string
        print(f"{item} -> {szotar[item]}")

def opcio2(dict):
    # A fő gond, hogy értékből nem tudjuk megkapni a kulcsot
    for item in dict.values():
        print(item)

def opcio3(dict):
    for item in dict.items(): # kulcs-érték párokat ad vissza (2 elemű tuple)
        print(item, type(item)) # ('alma', 'apple') <class 'tuple'>

    for key, value in dict.items():
        print(f"{key} -> {value}")

#opcio3(szotar)
#opcio2(szotar)
#opcio1(szotar)

szotar["könyv"] = "book" # Új elem hozzáadása

# Szerepel-e egy adott kulcs a dictionaryben?
if "billentyűzet" in szotar.keys():
    del szotar["billentyűzet"]
else:
    szotar["billentyűzet"] = "keyboard"
    """

with open(os.path.join(os.path.dirname(__file__), "forras", "story.txt"), encoding="utf-8") as f:
    szöveg = f.read()
    szöveg = szöveg.replace(".", "")
    szöveg = szöveg.replace(",", "")
    szöveg = szöveg.replace("\"", "")
    szöveg = szöveg.replace("'s", "")
    szöveg = szöveg.replace("\n", "")
    szöveg = szöveg.replace("?", "")
    szöveg = szöveg.replace("!", "")
    szöveg = szöveg.lower()
    szöveg = szöveg.split(" ")

word_counter = {}

for word in szöveg:
    if word in word_counter.keys():
        word_counter[word] += 1
    else:
        word_counter[word] = 1

# A dictionary nem rendezhető, mert nem számít az elemek sorrendje
#word_counter.sort()

# Ha mégis rendezni akarjuk, akkor alakítsuk listává, majd vissza dictionary-vé

word_counter = dict(sorted(list(word_counter.items()), key=lambda x: x[1], reverse=True))
print(word_counter)

# Átlagosan hányszor fordul elő egy szó?
összeg = 0
for key, value in word_counter.items():
    összeg += value
print(f"Egy szó átlagosan {round(összeg/len(word_counter),2)} alkalommal fordul elő.")


#random.seed(42)
players = []

for i in range(10):
    player = {}
    player["class"] = random.choice(["Mage", "Warrior", "Priest", "Paladin", "Rogue"])
    player["level"] = random.randint(1, 80)
    player["stamina"] = random.randint(50, 280)
    player["strength"] = random.randint(50, 280)
    player["intellect"] = random.randint(50, 280)
    player["armor"] = random.randint(50, 280)
    player["speed"] = random.randint(50, 280)
    players.append(player)

print(players)

#1. feladat: Írjuk ki a legmagasabb szintű játékost.

max_index = 0
for i in range(1, len(players)):
    if players[i]["level"] > players[max_index]["level"]:
        max_index = i
print("A legmagasabb szintű játékos:", players[max_index])

#2. feladat: Mennyi a játékosok átlagos intelligencia szintje?

összeg = 0
for item in players:
    összeg += item["intellect"]
print("A játékosok átlagos intelligenciája:", round(összeg/len(players), 2))

#3. feladat: Hány Warrior van a csapatban?

szamlalo = 0
for item in players:
    if item["class"] == "Warrior":
        szamlalo += 1

print(szamlalo, "Warrior van a csapatban")

#4. feladat: Van-e legalább 60-as szintű Paladin a játékosok között
van = False
for item in players:
    if item["class"] == "Paladin" and item["level"] >= 60:
        van = True
        break

if van:
    print("Van legalább 60-as szintű Paladin a csapatban.")
else:
    print("Nincs legalább 60-as szintű Paladin a csapatban.")

#5. feladat: Írjuk ki, hogy melyik class-ból hány darab van a csapatban?
class_counter = {}
for item in players:
    if item["class"] in class_counter.keys():
        class_counter[item["class"]] += 1
    else:
        class_counter[item["class"]] = 1

print(class_counter)



