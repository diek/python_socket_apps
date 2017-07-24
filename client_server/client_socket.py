import socket


def main():
    host = '127.0.0.1'
    port = 5001
    INPUT_MSG = "Send a msg to server( 'q' to quit)."

    client_socket = socket.socket()
    client_socket.connect((host, port))

    msg_server = input(INPUT_MSG)
    while msg_server != "q":
        client_socket.send(msg_server.encode())
        data = client_socket.recv(1024).decode()
        print("Message from server: {}".format(data))
        msg_server = input(INPUT_MSG)

    client_socket.close()


if __name__ == '__main__':
    main()
