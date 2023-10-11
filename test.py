import requests

url="https://gympie-swift-parrot-kaak.2.us-1.fl0.io/login"
data={
    "username":"ma",
    "password":"1234",
}
data=requests.post(url,data).json()
print(data)