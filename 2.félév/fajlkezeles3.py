import pandas as pd # (python -m) pip install pandas
import numpy as np  # pip install numpy
import os

FORRAS_PATH = os.path.dirname(__file__) # 2. félév mappa (nálam)
FORRAS_PATH = os.path.join(FORRAS_PATH, "forras") # forras mappa

pd.set_option('display.max_columns', None)

# Beolvasás, és fölösleges oszlopok törlése
data = pd.read_csv(os.path.join(FORRAS_PATH, "library.csv"))
print(data.columns) # Oszlopok nevei
data = data.drop(["Edition Statement", "Corporate Author", 'Corporate Contributors','Former owner','Engraver', 'Issuance type', 'Flickr URL', 'Contributors'], axis=1)
print(data.columns)
data = data.drop(columns=["Shelfmarks"])

# Indexeljük újra a táblázatot (DataFrame), az új sorindex legyen az Identifier értéke
print(data["Identifier"].is_unique) # Leelenőrizzük, hogy az Identifier unique (egyedi) - e
# True -> Minden Identifier egyedi -> alkalmas sorok indexelésére
data = data.set_index("Identifier")

print(data.loc[1143]) # 1143-as ID-ju könyvet kapjuk
print(data.iloc[1143]) # Ez már egy másik könyv ( 1143 + 1. könyv a táblázatban)
print(data.loc[1143, "Author"]) # A., T.
print(data.iloc[10, 4])         # nan

# Az adatok elég zavarosak, le kellene őket tisztítani
# Tisztítsuk le a Date of Publication és Place of Publication oszlopokat
#print(data["Date of Publication"].head(20))
year = data["Date of Publication"].str.extract(r"(\d{4})", expand = False)
data["Date of Publication"] = year.astype("Int16")
print(data.head(20))

# A hiányzó értékeket is kezeljük le valahogyan
print("null értékek száma (Date oszlop):", data["Date of Publication"].isnull().sum())
atlag = round(data["Date of Publication"].mean()) # 1859
data["Date of Publication"] = data["Date of Publication"].fillna(atlag)
print(data.head(20))


places = (data["Place of Publication"].str.replace(r"[\[\]]", "", regex=True)
            .str.split(r"[;,:]", n = 1).str[0].str.strip()  
        )
data["Place of Publication"] = places

print(data["Place of Publication"].head(100))
