"""
Author: Eren Sezener (erensezener@gmail.com)

Description: This demo program does sinusoidal movements.

"""

import socket
import time
import math


TCP_IP = '10.100.48.101'
TCP_PORT = 5005
BUFFER_SIZE = 1024

DELAY = 0.004
current_milli_time = lambda: int(round(time.time() * 1000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

w = 2 * math.pi * 0.2
amp = 5 * math.pi / 180.0
magic_number = 5.0 / 24.0

count = 0
prev_time = current_milli_time()
while True:
    time.sleep(0.004)
    count = count + 1
    t = 0.004 * count
    temp = str(magic_number * amp * w * math.cos(w * t))
    text = 'a,' + temp +',' + temp + ',' + temp + ',' + temp +',' + temp + ',' + temp
    s.send(text)
    data = s.recv(BUFFER_SIZE)
    cur_time = current_milli_time()
#    print cur_time - prev_time
    prev_time = cur_time

s.close()
