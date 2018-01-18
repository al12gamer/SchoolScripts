import socket, sys


def getHostnameByIP(h):
    print('You just hit my function')


    try:
        hostname = str(sys.argv[1])
        ip = socket.gethostbyname(hostname)
        print(hostname + ' has an IP of ' + ip)
    except:
        print("Oops, something is wrong with dat host boi.")

getHostnameByIP(sys.argv[1])
