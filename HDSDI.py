class HDSDI(object):
    '''This class is essentially a wrapper that holds a vision object and an audio object'''
    def __init__(self, vision, audios):
        self.vision = vision
        self.audios = audios

    def getVision(self):
        return self.vision

    def getAudios(self):
        return self.audios

    def setAudios(self, audios):
        self.audios = audios

    def setVision(self, vision):
        self.vision = vision