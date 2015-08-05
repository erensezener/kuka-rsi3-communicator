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

SEND_IP = '10.100.48.101'
SEND_PORT = 5005
RECEIVE_IP = '10.100.48.101'
RECEIVE_PORT = 49100 
BUFFER_SIZE = 1024

sockSend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockSend.connect((SEND_IP, SEND_PORT))


sockReceive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sockReceive.bind((RECEIVE_IP, RECEIVE_PORT))
f1 = open('./log.txt', 'w')
f2 = open('./log2.txt', 'w')

def receiveData():
    data, addr = sockReceive.recvfrom(1024)
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.fromstring(data, parser=parser)
    angles = tree[0].attrib
    refAngles = tree[1].attrib
    currents = tree[2].attrib
    tiem = time.time()
    if False :
        print >> f1, '{} {} {} {} {} {}'.format(currents['A1'], currents['A2'], currents['A3'], currents['A4'], currents['A5'], currents['A6'])
    if True :
        print >> f1, '{} {} {} {} {} {} {}'.format(angles['X'], angles['Y'], angles['Z'], angles['A'], angles['B'], angles['C'], tiem)
    if False :
        print >> f1, '{} {} {} {} {} {}'.format(angles['A1'], angles['A2'], angles['A3'], angles['A4'], angles['A5'], angles['A6'])

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


tEnd = 1.5
posStart = 00.0
posEnd = 00.0
posDepth = 300.0
while True:
    curTime = time.time() - startTime
    pos = traj.poly6(curTime, tEnd, posStart, posEnd, posDepth)
    radius = 100
    xPos = 0
    yPos = 0
    zPos = pos
    #yPos = radius*math.sin(curTime*2*math.pi*freq)
    #xPos = radius*(1-math.cos(curTime*2*math.pi*freq))
    text = 'r,'+str(xPos)+','+str(yPos)+','+str(zPos)+',0,0,0'
    sockSend.send(text)
    data = sockSend.recv(BUFFER_SIZE)
    receiveData()
    t = t + 0.004
    time.sleep(max(0, t - time.time()))
sockSend.close()
sockReceive.close()
