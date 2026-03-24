import requests

def get_weather(city:str) -> str:
    url = f"https://wttr.in/{city}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print("ERROR:", response.status_code)

weather = get_weather("Nagykanizsa")
print(weather)