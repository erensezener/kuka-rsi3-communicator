import socket

UDP_IP = "10.100.48.101" # IP Address of the External PC
UDP_PORT = 49152 # Port of the External PC
BUFFER_SIZE = 1024
XML_FILE_NAME = "ExternalData.xml"

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        xml_file = open(XML_FILE_NAME, "r")

        received_data, socket_of_krc = sock.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes
        print received_data
        data_to_send = xml_file.read()
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

    return data_to_send.replace("<IPOC>"+old_ipoc+"</IPOC>", "<IPOC>"+received_ipoc+"</IPOC>")

if __name__ == "__main__":
    main()