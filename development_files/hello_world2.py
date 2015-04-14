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
import math


TCP_IP = '10.100.48.101'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

w = 2 * math.pi * 0.1
amp = 3 * math.pi / 180.0

count = 0
while True:
    count = count + 1
    t = 0.004 * count
    text = 'a,' + str(amp * w * math.cos(w * t)) + ',' + str(amp * w * math.cos(w * t)) + ',' + str(amp * w * math.cos(w * t)) + ',' + str(amp * w * math.cos(w * t)) + ',' + str(amp * w * math.cos(w * t)) + ',' + str(amp * w * math.cos(w * t)) 
    s.send(text)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data

s.close()
