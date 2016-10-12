class HDSDI(object):
    def __init__(self):
        self.vision = {'Vision': True}
        self.audios = {'Audio 1': False, 'Audio 2':False}

    def getVision(self):
        return self.vision