from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

import configparser
import router
import parser

class HTTPServer:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.HOST, self.PORT = self.config['DEFAULT']['HOST'], int(self.config['DEFAULT']['PORT'])
        self.rootDir = self.config['STRUCTURE']['rootDir']
        self.ROUTER = router.Router()
        self.ROUTER.setRootDir(self.rootDir)

    def start(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            sock.bind((self.HOST, self.PORT))
            sock.listen(1)
            while True:
                try:
                    conn, addr = sock.accept()
                    req = conn.recv(1024).decode()
                    request = parser.Request(req)
                    print(request.url)
                    print(request.body)
                    conn.sendall(self.ROUTER.route(request.url))
                    conn.close()
                except Exception as E:
                    print(E)
