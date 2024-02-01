
class Request:

    def __init__(self, req):
        self.method, self.body, self.headers, self.url = self.parseRequest(req)

    def parseRequest(self, req):
        lines = req.split('\n')
        method = lines[0].split(' ')[0]
        url = lines[0].split(' ')[1]
        body = lines[len(lines)-1]
        headers = lines[1:len(lines)-2]
        return method, body, headers, url

