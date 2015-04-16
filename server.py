"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 17, 2014

Description: Communicates with the KUKA Controller.

Status: Works correctly.

Dependencies:

Known bugs: -

"""

import socket
import settings
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def send_robot_data(sock, data):
    if settings.BROADCAST_ROBOT_POSITION is False:
        pass
    else:
        sock.sendto(data, (settings.RECEIVER_IP, settings.RECEIVER_PORT))


def run_server(connection):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
    sock.bind((settings.SERVER_IP, settings.SERVER_PORT))
    xml_file = open(settings.XML_FILE_NAME, "r")
    default_command = xml_file.read()
    prev_time = current_milli_time()
    while True:
        current_time = current_milli_time()
        print current_time - prev_time 
        prev_time = current_time
        received_data, socket_of_krc = sock.recvfrom(settings.BUFFER_SIZE)  # buffer size is 1024 bytes
        send_robot_data(sock, received_data)
        if connection.poll():
            data_to_send = connection.recv()
            default_command = data_to_send
        else:  # send the default
            data_to_send = default_command
        data_to_send = mirror_timestamp(received_data, data_to_send)
        sock.sendto(data_to_send, socket_of_krc)

    xml_file.close()


# Updates the timestamp of the data to send based on the timestamp of the received data
def mirror_timestamp(received_data, data_to_send):
    ipoc_begin_index = received_data.index("<IPOC>")
    ipoc_end_index = received_data.index("</IPOC>")
    received_ipoc = received_data[ipoc_begin_index + 6: ipoc_end_index]

    old_ipoc_begin_index = data_to_send.index("<IPOC>")
    old_ipoc_end_index = data_to_send.index("</IPOC>")
    old_ipoc = data_to_send[old_ipoc_begin_index + 6: old_ipoc_end_index]

    return data_to_send.replace("<IPOC>" + old_ipoc + "</IPOC>", "<IPOC>" + received_ipoc + "</IPOC>")
