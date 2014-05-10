import socket
from BeautifulSoup import BeautifulSoup

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print addr
    # print ("received message:", data)
    ipoc_begin_tag_index = data.index("<IPOC>")
    ipoc_end_tag_index = data.index("</IPOC>")
    old_ipoc = data[ipoc_begin_tag_index + 6: ipoc_end_tag_index]
    print(old_ipoc)
    new_ipoc = str(int(old_ipoc) + 1).zfill(10)
    data = data.replace("<IPOC>"+old_ipoc+"</IPOC>", "<IPOC>"+new_ipoc+"</IPOC>")
    print(new_ipoc)
    # soup = BeautifulSoup(data)
    # soup = BeautifulSoup('<script>some JS</script>')
    # print (soup.SEN.DAT)
    sock.sendto(data, (UDP_IP, 5006))