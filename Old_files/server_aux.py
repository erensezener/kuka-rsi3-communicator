import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 49153

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data = "<IPOC>0000000000</IPOC>"

while True:
    sock.sendto(data, (UDP_IP, 49152))
    received_data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", received_data)

    ipoc_begin_tag_index = received_data.index("<IPOC>")
    ipoc_end_tag_index = received_data.index("</IPOC>")
    old_ipoc = received_data[ipoc_begin_tag_index + 6: ipoc_end_tag_index]
    new_ipoc = str(int(old_ipoc) + 1).zfill(10)
    data = "<IPOC>"+new_ipoc+"</IPOC>"
