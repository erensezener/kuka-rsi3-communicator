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

alpha = 0
flag = 0
while True:
    if flag == 0:
        alpha = alpha +1
        if alpha > 200:
            flag = 1
    else:
        alpha = alpha -1
        if alpha < -200:
            flag = 0
    #time.sleep(0.005)
    text = 'a,' + str(alpha*0.2) + ',0,0,0,0,0'
    s.send(text)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data

s.close()
