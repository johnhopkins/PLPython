class Resource(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

class IncomingLine(Resource):
    def __init__(self, name):
        self.name = name
        self.inUse = False
        self.destinations = []

class OutgoingLine(Resource):
    def __init__(self, name):
        self.name = name
        self.inUse = False
        self.source = ''

class Processor(Resource):
    def __init__(self, name):
        self.name = name
        self.inUse = False
        self.source = ''
        self.destinations = []

