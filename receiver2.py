import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

file = open("ExternalData.xml", "r")
data = file.read()

while True:
    sock.sendto(data, (UDP_IP, 5005))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
    # soup = BeautifulSoup(data)
    # soup = BeautifulSoup('<script>some JS</script>')
    # print (soup.SEN.DAT)
