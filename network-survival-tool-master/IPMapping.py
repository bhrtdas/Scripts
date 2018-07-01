import socket

targetip = input('What is the domain you want to target? ')  

hostip = socket.gethostbyname(targetip)

print("The IP address of target is:", hostip)
