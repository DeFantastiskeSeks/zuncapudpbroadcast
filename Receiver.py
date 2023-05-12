from socket import *
import requests
import json
arr = []
serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ("", serverPort)
serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    uv, clientAddress = serverSocket.recvfrom(2048)
    print(uv)
    uvRecord = uv.decode()

    print("Received message:" + uvRecord)
    uvLoad = json.loads(uvRecord)

    for i in uvLoad.values():
        arr.append(i)
    print(arr)
    if(arr.len() > 4):
       arraysum = sum(arr)





    #api_url = "https://speedtrapapi20230411142537.azurewebsites.net/api/SpeedTraps"
    #request = requests.post(api_url, json=speedTrapDe)