from socket import *
import random
import json
from time import sleep

serverName = '255.255.255.255'
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    uv = round(random.uniform(3.5, 5.0), 1)

    uvInfo = { "uv": uv}
    uvJson = json.dumps(uvInfo)

    clientSocket.sendto(uvJson.encode(), (serverName, serverPort))
    print("send file")
    print(uv)
    sleep(2)