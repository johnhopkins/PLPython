from match import *
from gallery import *
from matchday import *
from tielines import *
from feed import *
from plan import *
from audio import *

'''All the following to be webified!'''

matchDate = raw_input('Matchday Date ')
matchDayInstance = MatchDay(matchDate)
numberOfMatches = int(raw_input('Number of matches? '))

for match in range(numberOfMatches):

    print '========== Match ' + str(match + 1) + ' =========='
    homeTeam = raw_input('Home Team ')
    awayTeam = raw_input('Away Team ')
    kickOffTime = raw_input('Kick Off Time ')
    hostBroadcaster = raw_input('Host Broadcaster ')

    matchDayInstance.addMatch((Match(homeTeam, awayTeam, kickOffTime, hostBroadcaster)))


a = Tieline()
b = Tieline()
c = Tieline()

print(Tieline.availableTielines)

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