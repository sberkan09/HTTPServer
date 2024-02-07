

class Router:
    paths = [
        ("/404-NOTFOUND", "server_pages/404.html"),
        ("/inDevelopment", "server_pages/inDevelopment.html"),
    ]
    rootDir = "./"
    def __init__(self):
        pass

    def setRootDir(self, rootPath):
        Router.rootDir = rootPath

    def add(self, url, path):
        Router.paths.append((url, path))
    
    def route(self, method, url, body):
        for path in Router.paths:
            if (path[0] == url):
                return self.wrapper(path[1])
        return self.wrapper(Router.paths[0][1], True)

    def wrapper(self, path, nf=False):
        if (nf):
            return b"HTTP/1.1 404 Not Found\n\n" + self.content(path) + b"\n"
        else:
            return b"HTTP/1.1 200 OK\n\n" + self.content(path) + b"\n"

    def content(self, path):
        try:
            with open(Router.rootDir + path, mode='rb') as file:
                return file.read()
        except FileNotFoundError as E:
            return self.content(Router.paths[1][1])