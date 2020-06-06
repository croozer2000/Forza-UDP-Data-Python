import socket
import struct

def convert_bytes_to_type(fmt, index, message):
    '''Converts 4 byte increments to the correct data type
    Forza sends data as little endian'''
    
    if fmt == "f32":
        return struct.unpack('<f',message[index:index+4])
    else: #other types used is u32,s32,u8,s8
        return int.from_bytes(message[index:index+4],"little")
    

localIP     = "192.168.8.220"
localPort   = 10443
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams


while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    # message1 = int.from_bytes(message[0:4],"little")
    # message2 = struct.unpack('<f',message[4:8])

    print(convert_bytes_to_type("u32",0,message))


   

