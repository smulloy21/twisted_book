from twisted.internet.defer import Deferred

def addBold(msg):
    return "<b>%s</b>" % (msg,)

def addItalic(msg):
    return "<i>%s</i>" % (msg,)

def printHTML(msg):
    print msg

d = Deferred()
d.addCallback(addItalic)
d.addCallback(addBold)

d.addCallback(printHTML)

d.callback('Yo.')
