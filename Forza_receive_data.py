import socket
import struct
from ForzaCar import convert_bytes_to_type, ForzaCarStats, gauge_bar


    

localIP     = "192.168.8.220"
localPort   = 10443
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams

# oredered list of forza packet structure
packet_struct = ["s32","u32","f32","f32","f32"]
packet_item_variables = ["IsRaceOn","TimestampMS","EngineMaxRpm","EngineIdleRpm","CurrentEngineRpm","AccCarX","AccCarY","AccCarZ"]



while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    # loop through item list and append values to ordered list
    # count = 0
    # item_list = []
    # for item in packet_struct:
    #     item_list.append(convert_bytes_to_type(item,count*4,message))
    #     count += 1

    # create new ForzaCarStats items and initalizq data
    carNow = ForzaCarStats(message)

    # print out engine RPM and terminal gauge bar
    print(f'Engine RPM: {carNow.CurrentEngineRpm[0]:8.2f} [{gauge_bar(carNow.CurrentEngineRpm[0],10000)}]\r', end="")


   

