# El método POST sirve para crear nuevos recursos en el servidor

import requests

URL = "https://httpbin.org/post"

data = {
    'username': 'Daniel',
    'password': 1234
}

response = requests.post(URL, data=data)

if response.status_code == 200:
    payload = response.json()
    print(response.text)
    print(response.url)