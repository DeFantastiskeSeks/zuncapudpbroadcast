from socket import *
import requests
import json
arr = []
serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ("", serverPort)
serverSocket.bind(serverAddress)
print("The server is ready")

userInfo = { "name": "simon"}

while True:
    uv, clientAddress = serverSocket.recvfrom(2048)
    uvRecord = uv.decode()

    uvLoad = json.loads(uvRecord)
    
    for i in uvLoad.values():
        arr.append(i)
        
    print(arr)
    
    if(len(arr) > 99):
        arrsum = round(sum(arr) / 100, 1)
        print(arrsum)
        sumParams = {"UV": arrsum}
        api_url = "https://zuncapapi.azurewebsites.net/api/Users/exposure"
        request = requests.post(api_url, params=sumParams, json=userInfo)
        print(request.status_code)
        print(request.text)
        arr.clear()