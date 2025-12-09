import os
import csv
import pandas as pd # pip install pandas (terminálba)
import matplotlib.pyplot as plt # pip install matplotlib
import folium # pip install folium

#print(f"__file__: {__file__}")
#print(f"dirname(__file__): {os.path.dirname(__file__)}")

PATH_FORRAS = os.path.join(os.path.dirname(__file__), "forras")

def opcio1():
    matrix = []
    with open(os.path.join(PATH_FORRAS, "directory.csv"), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(',')
            matrix.append(line)

#opcio1()

def opcio2():
    matrix = []
    with open(os.path.join(PATH_FORRAS, "directory.csv"), "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter = ",")
        for row in data:
            matrix.append(row)

#opcio2()

def opcio3():
    data = pd.read_csv(os.path.join(PATH_FORRAS, "directory.csv"))
    return data

# Brand,Store Number,Store Name,Ownership Type,Street Address,City,
# State/Province,Country,Postcode,Phone Number,Timezone,Longitude,Latitude

data = opcio3()
print(type(data)) # <class 'pandas.core.frame.DataFrame'>

data = data[["Store Name","Street Address", "City", "Country", "Postcode", "Longitude", "Latitude"]]

magyarok = data[data["Country"] == "HU"]
chicagoiak = data[data["City"] == "Chicago"]

print(data.iloc[5, 2]) # Abu Dhabi (5. sor, 2. oszlopa)
print(data.loc[5242, "City"]) # Paris

print(data.iloc[10, :])

orszagonkent = data.groupby("Country").count().reset_index("Country")
orszagonkent = orszagonkent[["Country", "Store Name"]]
orszagonkent.columns = ["Country", "Count"]
orszagonkent = orszagonkent.sort_values(by="Count", ascending=False)
orszagonkent = orszagonkent[orszagonkent["Count"] >= 35]
orszagonkent = orszagonkent[orszagonkent["Count"] < 1000]
print(orszagonkent)

def store_count_per_country_plot(df):
    plt.bar(df["Country"], df["Count"])
    plt.xticks(rotation=90)
    plt.show()

def show_on_map(df):
    row = df.iloc[0, :]
    map = folium.Map(location=[row.loc["Latitude"], row.loc["Longitude"]], tiles = "cartoDb positron")

    df.apply(
        lambda row: folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=10,
            fill=True,
            color="red",
            popup=row["Store Name"]
        ).add_to(map), axis = 1
    )
    # 47.4979° N, 19.0402° E
    folium.Marker(location=[47.4739, 19.2713], popup="Logiscool Rákoskeresztúr").add_to(map) 

    map.show_in_browser()

#store_count_per_country_plot(orszagonkent)
show_on_map(magyarok)