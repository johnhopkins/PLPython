class Feed(object):

    def __init__(self, name, incomingline, tieline, hdsdi):
        self.hdsdi = hdsdi
        self.name = name
        self.incomingline = incomingline
        self.tieline = tieline