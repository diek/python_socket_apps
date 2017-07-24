import socket
from config import BaseConfig as cfg


def main():

    server_socket = socket.socket()
    server_socket.bind((cfg.HOST, cfg.PORT))

    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print("Connection from: {}".format(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client: {}".format(data))
        data = input("Send some data to client: ")
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    main()
