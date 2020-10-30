##ex.1 create an echo server that replies to a client message with the same message
##server 
import socket
import sys
import subprocess

HOST = ''
PORT = 50000

if __name__ == "__main__":
    while True:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        command = data.split()[0]
        if command == 'echo':
            if len(data.split()) > 1:
                process = subprocess.Popen(['echo', data.split()[1]],
                                     stdout = subprocess.PIPE,
                                     stderr = subprocess.PIPE)
                stdout, stderr = process.communicate()
                conn.send(stdout)
                conn.send(stderr)
        elif command == 'ls':
            process = subprocess.Popen('ls',
                                     stdout = subprocess.PIPE,
                                     stderr = subprocess.PIPE)
            stdout, stderr = process.communicate()
            conn.send(stdout)
            conn.send(stderr)                    
            response = "\n"
            ##for elem in stdout:
            ##    response += str(elem)
            ##    response += "\n"
            ##conn.send(response.encode())
        else:
            conn.send("help".encode()) 
        ##conn.close()
        



    
