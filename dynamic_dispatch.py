from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site

from calendar import calendar

from datetime import datetime   # for home page redirect
from twisted.web.util import redirectTo # for home page redirect

class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)

class CalendarHome(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()

    # def render_GET(self, request): # static home page
    #     return "<html><body>Welcome to the calendar server!</body><html>"

    def render_GET(self, request): # for home page redirect
        return redirectTo(str(datetime.now().year), request)

root = CalendarHome()
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
