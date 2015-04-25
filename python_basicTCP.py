import socket
import sys
TCP_IP = input("IP ADDRESS:")

TCP_PORT = int(input("UDP PORT:"))


print ("TCP target IP:", TCP_IP)

print ("TCP target port:", TCP_PORT)
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
while True:




    while True:
        newin = input("send command:")
        print (newin)
        if newin == "exit":
            sock.close()
            sys.exit()
        else:
            sock.send(newin.encode('utf-8'))
            sock.settimeout(1.5)
            try:
                d = sock.recv(BUFFER_SIZE)

            except socket.timeout:
                break
            else:
                #data = d[0]
                #addr = d[1]
                print (d.decode('utf-8'))

