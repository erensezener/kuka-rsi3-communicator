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
current_milli_time = lambda: int(round(time.time() * 1000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

w = 2 * math.pi * 0.5
amp = 5 * math.pi / 180.0

count = 0
prev_time = current_milli_time()
while True:
#    time.sleep(0.0045)
    count = count + 1
    t = 0.004 * count
    text = 'a,' + str(amp * w * math.cos(w * t)) + ',0,0,0,0,0'
    s.send(text)
    data = s.recv(BUFFER_SIZE)
    cur_time = current_milli_time()
    print cur_time - prev_time
    prev_time = cur_time

s.close()
