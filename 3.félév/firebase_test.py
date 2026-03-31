import requests
import time

url = "https://snake-kedd-default-rtdb.europe-west1.firebasedatabase.app/highscores.json"

def get_highscores():
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("ERROR:", response.status_code)

def post_highscore(name, score):
    data = {
        "name":name,
        "score":score,
        "timestamp": int(time.time())
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print("ERROR:", response.status_code)

print(post_highscore("asd", 3))
print(get_highscores())