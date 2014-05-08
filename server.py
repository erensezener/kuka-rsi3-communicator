import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 49152
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def update_timestamp(recieved_data, data_to_send):
    ipoc_begin_index = recieved_data.index("<IPOC>")
    ipoc_end_index = recieved_data.index("</IPOC>")
    recieved_ipoc = recieved_data[ipoc_begin_index + 6: ipoc_end_index]

    old_ipoc_begin_index = data_to_send.index("<IPOC>")
    old_ipoc_end_index = data_to_send.index("</IPOC>")
    old_ipoc = data_to_send[old_ipoc_begin_index + 6: old_ipoc_end_index]

    return data_to_send.replace("<IPOC>"+old_ipoc+"</IPOC>", "<IPOC>"+recieved_ipoc+"</IPOC>")


while True:
    xmlFile = open("ExternalData.xml", "r")

    recieved_data, socket_of_krc = sock.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes

    data_to_send = xmlFile.read()
    data_to_send = update_timestamp(recieved_data, data_to_send)

    sock.sendto(data_to_send, socket_of_krc)

    xmlFile.close()
