from SocketServer import BaseRequestHandler, TCPServer
from socket import socket, AF_INET, SOCK_STREAM
import sys

class SockHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print("Passing data from: " + str(self.client_address[0]) + " to " + external_LAN_IP)
        print(self.data)

        # Create a socket to connect to the external server
        external_socket = socket(AF_INET, SOCK_STREAM)
        try:
            # Connect to the external server
            external_socket.connect((external_LAN_IP, external_LAN_PORT))
            external_socket.sendall(self.data)

            # Continuously receive commands from the external server and send them back to the client
            while True:
                command = external_socket.recv(1024)
                if not command:
                    break
                self.request.sendall(command)
        finally:
            external_socket.close()

if __name__ == '__main__':
    private_LAN_IP, private_LAN_PORT, external_LAN_IP, external_LAN_PORT = sys.argv[1:]

    # Convert ports to integers
    private_LAN_PORT = int(private_LAN_PORT)
    external_LAN_PORT = int(external_LAN_PORT)

    # Start the TCP server
    myserver = TCPServer((private_LAN_IP, private_LAN_PORT), SockHandler)
    myserver.serve_forever()
