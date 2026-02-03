# A dictionary (szótár) adatszerkezet

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