import socket


def main():
    host = '127.0.0.1'
    port = 5001

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print("Connection from: {}".format(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: {}".format(data))
        print("Received from User: {}".format(data))
        data = input("Send some data: ")
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    main()
