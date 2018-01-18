import socket

hosts = ['www.uc.edu', 'www.google.com', 'www.bing.com']
for h in hosts:
    print(h + ':\t\t' + socket.gethostbyname(h))
