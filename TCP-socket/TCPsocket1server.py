##ex.1 create an echo server that replies to a client message with the same message
##server 
import socket
import sys

HOST = ''
PORT = 50000

if __name__ == "__main__":
    while True:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((HOST, PORT))
        print()
        serversocket.listen(5)
        conn, addr = serversocket.accept()
        print(f"addr: {addr}")
        print(f"conn: {conn}")
        data = conn.recv(1024)
        data = data.decode()
        if data is None: break
        print(data)
        if data.split()[0] == 'echo':
            if len(data.split()) > 1: conn.send(data.split()[1].encode())
        conn.close()
        



    
