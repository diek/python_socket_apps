import socket

from config import BaseConfig as cfg


def main():
    client_socket = socket.socket()
    client_socket.connect((cfg.HOST, cfg.PORT))

    msg_server = input(cfg.INPUT_MSG)
    while msg_server != "q":
        client_socket.send(msg_server.encode())
        data = client_socket.recv(1024).decode()
        print("Message from server: {}".format(data))
        msg_server = input(cfg.INPUT_MSG)

    client_socket.close()


if __name__ == '__main__':
    main()
