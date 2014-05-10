import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

file = open("ExternalData.xml", "r")
xml_string = file.read()

print xml_string
# print "UDP target IP:", UDP_IP
# print "UDP target port:", UDP_PORT
# print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(xml_string, (UDP_IP, UDP_PORT))