##ex.1 create an echo server that replies to a client message with the same message
##server 
import socket
import sys
import subprocess

help_msg = ("command list: \n - print <msg>: echo <msg>\n" 
            " - ls: list files\n"
            " - cat <file1>...<fileN>: concatenate files\n"
            " - help: show command lists\n")

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
        if command == 'print':
            echo_msg=[]
            for elem in data.split()[1:]:
                echo_msg.append(elem)
            if len(data.split()) > 1:
                process = subprocess.Popen(['echo', echo_msg],
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
        elif command == 'cat':
            cat_cmd=[]
            for elem in data.split():
                cat_cmd.append(elem)
            process = subprocess.Popen(cat_cmd,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE)
            stdout, stderr = process.communicate()
            conn.send(stdout)
            conn.send(stderr)
        else:
            conn.send(help_msg.encode()) 
        ##conn.close()
        



    
