class AudioChannel(object):

    def __init__(self, name, LR):
        self.name = name
        self.LR = LR

class AudioPair(object):

    def __init__(self, audio1, audio2):
        self.audio1 = audio1
        self.audio2 = audio2

class AudioGroup(object):

    def __init__(self, pair1, pair2):
        self.pair1 = pair1
        self.pair2 = pair2

class Audio(object):

    def __init__(self, group1, group2, group3, group4):
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.group4 = group4

a = Audio()
