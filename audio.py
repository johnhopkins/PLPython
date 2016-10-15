class AudioChannel(object):

    def __init__(self, name):
        self.name = name

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

a = AudioChannel('International L')
b = AudioChannel('International R')
c = AudioChannel('Mute')
d = AudioChannel('Mute')
pair = AudioPair(a, b)
pair2 = AudioPair(c, d)
group1 = AudioGroup(pair, pair2)

print(group1.pair1.audio1.name)
print(group1.pair1.audio2.name)
print(group1.pair2.audio1.name)
print(group1.pair2.audio2.name)