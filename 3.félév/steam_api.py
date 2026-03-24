import requests

url_base = "https://valvesoftware.com/"

def get_players():
    url = url_base + "about/stats/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("ERROR:", response.status_code)


def get_results():
    url = "https://store.steampowered.com/search/results/?json=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("ERROR:", response.status_code)




player_info = get_players()

print(f"Jelenleg {player_info['users_online']} ember van online.")
print(f"Ebből {player_info['users_ingame']} van játékban.")

jatekok = get_results()

print("Az 5 legnépszerűbb játék a steam-en:")
i = 1
for game in jatekok['items']:
    print(f"{i}.: {game['name']}")
    i += 1
    if i >= 6:
        break



def get_csgo_item_prices(appid:int, item:str):
    # 730 = Counter-Strike 2 APPID
    # currency = 3 = EUR (1 USD)
    # start = 0    - legolcsóbb elől
    url = f"https://steamcommunity.com/market/listings/{appid}/{item}/render?currency=1&start=0"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("HIBA:", response.status_code)


#https://steamcommunity.com/market/listings/227300/Spooky%20Horn

appid = 227300 # cs 2
item = "Spooky%20Horn"

prices = get_csgo_item_prices(appid, item)

print("Elérhető Spooky%20Horn-ok:")
for key, item in prices['listinginfo'].items():
    print(f"{item['price'] / 100} $")



