"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 22, 2014

Description: This demo program moves the 5th joint.

Status: Works correctly.

Dependencies:

Known bugs: -

"""

import socket
import time


TCP_IP = '10.100.48.101'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

count = 0
flag = 0
while True:
    if flag == 0:
        count = count +1
        if count > 200:
            flag = 1
    else:
        count = count -1
        if count < -200:
            flag = 0
    text = 'a,' + str(0.05) + ',0,0,0,0,0'
    s.send(text)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data

s.close()
