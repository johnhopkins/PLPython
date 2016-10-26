class AudioChannel(object):

    def __init__(self, name):
        self.name = name

class AudioPair(object):

    def __init__(self, audio1, audio2):
        assert isinstance(audio1, AudioChannel), 'AudioPair object only takes objects of type AudioChannel'
        assert isinstance(audio2, AudioChannel), 'AudioPair object only takes objects of type AudioChannel'
        self.audio1 = audio1
        self.audio2 = audio2

class AudioGroup(object):

    def __init__(self, pair1, pair2):
        assert isinstance(pair1, AudioPair), 'AudioGroup object only takes objets of type AudioPair'
        assert isinstance(pair2, AudioPair), 'AudioGroup object only takes objets of type AudioPair'
        self.pair1 = pair1
        self.pair2 = pair2

class Audio(object):

    def __init__(self, group1, group2, group3, group4):
        assert isinstance(group1, AudioGroup), 'Audio object only takes objets of type AudioPair'
        assert isinstance(group2, AudioGroup), 'Audio object only takes objets of type AudioPair'
        assert isinstance(group3, AudioGroup), 'Audio object only takes objets of type AudioPair'
        assert isinstance(group4, AudioGroup), 'Audio object only takes objets of type AudioPair'
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.group4 = group4


'''Testing code'''

a = AudioChannel('Channel 1')
b = AudioChannel('Channel 2')
c = AudioPair(a,b)
d = AudioGroup(c,c)
e = Audio(d,d,d,d)

print(e.group1.pair1.audio1.name)
print(e.group4.pair2.audio2.name)