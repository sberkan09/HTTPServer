import http
from router import Router

server = http.HTTPServer()

router = Router()
router.add("/post", "post.html")
router.add("/", "index.html")
router.add("/about", "about.html")

server.start()
