import requests
response = requests.get("http://local:5001")
print(response.text)
