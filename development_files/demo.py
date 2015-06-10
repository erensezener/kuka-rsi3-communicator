"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 22, 2014

"""

import socket
import time


TCP_IP = '10.100.48.101'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

count = 0
flag = -1
while True:
    if flag == 1:
        count = count +1
        if count > 50:
            flag = -1
    else:
        count = count -1
        if count < -50:
            flag = 1
    text = 'a,' + str(flag*0.15) + ',0,0,0,0,0'
    s.send(text)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data

s.close()
