from twisted.web import server, resource
from twisted.internet import reactor
import codecs
f = codecs.open("hello.html", 'r')

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return f.read()

site = server.Site(Simple())
reactor.listenTCP(8000, site)
reactor.run()
