"""
Description: Prints the latest config of the manipulator.

Author: Eren Sezener (erensezener@gmail.com)

Dependencies: Elementtree

"""

import socket
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

UDP_IP = '10.100.48.101'
UDP_PORT = 49100

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
# positions =[]


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print parse_positions(data)['A1']
    # positions.append(parse_positions(data).values())
    

# returns a dictionary where the keys are 'A1', 'A2' .. 'A6'
def parse_positions(xml_line):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.fromstring(xmlstring, parser=parser)
    return tree[0].attrib
    
def plot():
    array = np.array(positions)
    plt.plot(array)
    plt.show()
    