##create an echo server that replies to a client message executing echo/ls/cat/help 
import socket
import sys
import subprocess

help_msg = ("command list: \n - print <msg>: echo <msg>\n" 
            " - ls: list files\n"
            " - cat <file1>...<fileN>: concatenate files\n"
            " - help: show command lists\n")

HOST = ''
PORT = 50000

def cmdex(cmd, args):
    process = subprocess.Popen([cmd, args],
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    stdout, stderr = process.communicate()
    conn.send(stdout)
    conn.send(stderr)

if __name__ == "__main__":
    while True:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind((HOST, PORT))
        serversocket.listen(5)
        conn, addr = serversocket.accept()
        data = conn.recv(1024)
        data = data.decode()
        if data is None: break
        print(data)
        command = data.split(' ',1)   ## single split, separate command from arguments/paths 
        if command[0] == 'print':
            if len(command)<2:command.append("")
            cmdex('echo', command[1])
        elif command[0] == 'list':
            if len(command)<2:command.append("./")
            cmdex('ls', command[1])
        elif command[0] == 'concat':
            if len(command)<2:command.append("")
            cmdex('cat', command[1])
        else: 
            conn.send(help_msg.encode()) 


