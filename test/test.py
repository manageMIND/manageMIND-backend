import requests

BASE = "http://localhost:5000/"

#response = requests.get(BASE + "users")
#print(response)
#print(response)
#resp = requests.post("http://localhost:5000/predict")

getUser = requests.get("http://localhost:5000/users")
#postUser = requests.post("http://localhost:5000/users")
#print(resp.text)

print(getUser)