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
    #print(uv)
    uvRecord = uv.decode()

    #print("Received message:" + uvRecord)
    uvLoad = json.loads(uvRecord)
    
    for i in uvLoad.values():
        arr.append(i)
        
    print(arr)
    
    if(len(arr) > 4):
        arrsum = round(sum(arr) / 5, 1)
        print(arrsum)
        sumParams = {"UV": arrsum}
        api_url = "https://zuncapapi.azurewebsites.net/api/Users/exposure"
        request = requests.post(api_url, params=sumParams, json=userInfo)
        print(request.status_code)
        print(request.text)
        arr.clear()