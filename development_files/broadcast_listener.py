"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 17, 2014

Description: Listens to the KUKA Positions.

Status: Works correctly.

Dependencies:

Known bugs: -

"""

import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 49100

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
