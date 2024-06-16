import requests
import json

url = "https://reqres.in/api/register"

payload = json.dumps({
    "email": "eve.holt@reqres.in",
    "password": "pistol"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
