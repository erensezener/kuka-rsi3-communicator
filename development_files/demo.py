"""
Author: Eren Sezener (erensezener@gmail.com)

Description: This demo program does sinusoidal movements.

"""

import socket
import time
import math
import thread
import threading
import xml.etree.ElementTree as ET

import generateTrajectory as traj

TCP_IP = '10.100.48.101'
TCP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))



def listenKuka():

    UDP_IP = '10.100.48.101'
    UDP_PORT = 49100 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    
    while True:
        data, addr = sock.recvfrom(1024)
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.fromstring(data, parser=parser)
        angles = tree[0].attrib
        tiem = time.time()
        if True :
            print '{} {} {} {} {} {}'.format(angles['X'], angles['Y'], angles['Z'], angles['A'], angles['B'], angles['C'])
        if False :
            print '{} {} {} {} {} {}'.format(angles['A1'], angles['A2'], angles['A3'], angles['A4'], angles['A5'], angles['A6'])
thread.start_new_thread(listenKuka, ())

freq = 0.3


t = time.time()
startTime = t
while False:
    curTime = time.time() - startTime
    angle = (1-math.cos(curTime*2*math.pi*freq))*10
    text = 'a,'+str(angle)+','+str(angle)+','+str(angle)+','+str(angle)+','+str(-2*angle)+','+str(angle)
    sock.send(text)
    data = sock.recv(BUFFER_SIZE)
    t = t + 0.004
    time.sleep(max(0, t - time.time()))


tEnd = 5.0
posStart = 00.0
posEnd = 00.0
posDepth = 200.0
while True:
    curTime = time.time() - startTime
    pos = traj.poly6(curTime, tEnd, posStart, posEnd, posDepth)
    radius = 100
    xPos = pos
    yPos = pos
    zPos = pos
    #yPos = radius*math.sin(curTime*2*math.pi*freq)
    #xPos = radius*(1-math.cos(curTime*2*math.pi*freq))
    text = 'r,'+str(xPos)+','+str(yPos)+','+str(zPos)+',0,0,0'
    sock.send(text)
    data = sock.recv(BUFFER_SIZE)
    t = t + 0.004
    time.sleep(max(0, t - time.time()))
sock.close()
