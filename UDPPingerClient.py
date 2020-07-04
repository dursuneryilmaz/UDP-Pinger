# Import socket module
# Import time and ctime to retrieve time
# Import sys to retrieve the arguments
from socket import *
from time import time, ctime
import sys


# Preparing the socket
serverHost, serverPort = sys.argv[1:]
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
print("\nDursun ERYILMAZ 151805011")
print("Ülkü ÇOR 151805024\n")
for i in range(100):
    startTime = time() # Retrieve the current time
    message = "Ping " + str(i+1) + " " + ctime(startTime)[11:19]

    try:
        # Sending the message and waiting for the answer
        clientSocket.sendto(message.encode(),(serverHost, int(serverPort)))
        encodedModified, serverAddress = clientSocket.recvfrom(1024)

        # Checking the current time and if the server answered
        endTime = time()
        modifiedMessage = encodedModified.decode()
        print(modifiedMessage)
        print("RTT: %f ms\n" % ((endTime - startTime)*1000))
    except:
        print("Request timed out\n")

print("\nDursun ERYILMAZ 151805011")
print("Ülkü ÇOR 151805024\n")
clientSocket.close()
