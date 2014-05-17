"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 17, 2014

Description: Sends updates to the server through TCP.

Status: Works correctly.

Dependencies:

Known bugs: -

"""

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = 'r,0,0,0,0,0,0'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    input_text = raw_input("Enter a command: ")
    s.send(input_text)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data

s.close()

