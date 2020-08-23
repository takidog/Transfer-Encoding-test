import socketserver

import socket


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024).strip()

        print("request raw body : {raw}".format(raw=self.data))
        # response by [curl -i --raw]
        data = open('raw_response.data', 'rb').read()
        # print(data)
        self.request.send(data)


if __name__ == "__main__":

    HOST, PORT = socket.gethostname(), 5433

    print('HOST: ', HOST)

    print('Port: ', PORT)

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()
