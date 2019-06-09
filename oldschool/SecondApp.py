import requests
params = {
    'secret' : "super duper top secret"
}
r = requests.get(url="http://127.0.0.1:5000/", params=params)
print(r.text)
