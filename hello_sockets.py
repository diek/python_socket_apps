# hello_sockets.py

import socket
import sys

"""sock_obj = socket.socket(socket_family, socket_type, protocol=0)
socket_family: defines the family of protocols used as the transport mech
    1. AF_UNIX; or
    2. AF_INET
socket_type: defines the communication between the two end-points
    1. SOCKET_STREAM - connection-oriented protocols,e.g. Transmission Control Protocol (TCP),
                                                          Stream Control Transmission Protocol (SCTP) or
                                                          Datagram Congestion Control Protocol (DCCP)
    2. SOCK_DGRAM - connectionless protocols, e.g. User Datagram Protocol (UDP)
protocol: blank or set to zero
"""

try:
    # Instantiate and AF_INET, STREAM socket(TCP)
    sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print('Unable to instantiate socket. Error code: {} , Error message : {}'.format(err_msg[0], err_msg[1]))
    sys.exit()

print('hello socket')
