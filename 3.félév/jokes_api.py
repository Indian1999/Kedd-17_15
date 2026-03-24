import requests

url = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.text # '{"type":"programming","setup":"Why ... nature?","punchline":"Too.. bugs.","id":440}'
        joke = response.json() # <class 'dict'>
        
        print(f"{joke['id']}: {joke['setup']}")
        print(joke['punchline'])
    else:
        print("ERROR:", response.status_code)

get_joke()