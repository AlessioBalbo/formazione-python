##ex.1 create an echo server that replies to a client message with the same message 
import socket
import sys

HOST = "127.0.0.1"
PORT = 50000

if __name__ == "__main__":
    ## command input
    while True:
        msg = input(f"enter command to sent to server {HOST}-{PORT}:")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("connected to server!")
        s.send(msg.encode())
        response = s.recv(1024)
        print(f"client message: {msg}")  
        print(f"server response: {response.decode()}")
        s.close()




    
