from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.static import File

root = Resource()
root.putChild('hello', File('/twisted_book/hello'))
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
