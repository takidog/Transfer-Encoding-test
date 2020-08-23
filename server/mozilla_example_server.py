import socketserver

import socket


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024).strip()

        print("request raw body : {raw}".format(raw=self.data))

        self.request.send(b"HTTP/1.1 200 OK\r\n")
        self.request.send(b"Content-Type: text/plain\r\n")
        # self.request.send(b"Connection: Close\r\n")
        self.request.send(b"Transfer-Encoding: chunked\r\n")
        self.request.send(b"\r\n")
        self.request.send(b"7\r\n")
        self.request.send(b"Mozilla\r\n")
        self.request.send(b"9\r\n")
        self.request.send(b"Developer\r\n")
        self.request.send(b"7\r\n")
        self.request.send(b"Network\r\n")
        self.request.send(b"0\r\n\r\n")
        self.request.close()


if __name__ == "__main__":

    HOST, PORT = socket.gethostname(), 5432

    print('HOST: ', HOST)

    print('Port: ', PORT)

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()
