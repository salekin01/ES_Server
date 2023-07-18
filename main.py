# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.140', 1111)  # Server IP and port
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server is listening for connections...")

    while True:
        connection, client_address = server_socket.accept()
        print("Connection established with:", client_address)

        data = connection.recv(1024).decode('utf-8')
        print("Received data:", data)

        response = "Message received successfully!"
        connection.sendall(response.encode('utf-8'))

        connection.close()


if __name__ == "__main__":
    start_server()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#     # Create a TCP/IP socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Bind the socket to the port
#     server_address = ('localhost', 10000)
#     # print >> sys.stderr, 'starting up on %s port %s' % server_address
#     print('starting up on %s port %s' % server_address, file=sys.stderr)
#     sock.bind(server_address)
#
#     # Listen for incoming connections
#     sock.listen(1)
#
#     while True:
#         # Wait for a connection
#         # print >> sys.stderr, 'waiting for a connection'
#         print('waiting for a connection', file=sys.stderr)
#         connection, client_address = sock.accept()
#
#         try:
#             # print >> sys.stderr, 'connection from', client_address
#             print('connection from', client_address, file=sys.stderr)
#
#             # Receive the data in small chunks and retransmit it
#             while True:
#                 data = connection.recv(16)
#                 # print >> sys.stderr, 'received "%s"' % data
#                 print(f'received "{data}"', file=sys.stderr)
#                 if data:
#                     # print >> sys.stderr, 'sending data back to the client'
#                     print('sending data back to the client', file=sys.stderr)
#                     connection.sendall(data)
#                 else:
#                     # print >> sys.stderr, 'no more data from', client_address
#                     print('no more data from', client_address, file=sys.stderr)
#                     break
#
#         finally:
#             # Clean up the connection
#             connection.close()
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
