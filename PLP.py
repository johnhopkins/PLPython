from match import *
from gallery import *
from matchday import *
from data import *
from resources import *
from tielines import *

a = Tieline()
b = Tieline()
c = Tieline()
d = Tieline()
f = Tieline()
g = Tieline()
h = Tieline()
i = Tieline()
j = Tieline()

print(a.tielineNumber())
print(i.tielineNumber())

print(b.howMany())

# gallery3 = Gallery()
#
# print(gallery3.getAvailableExternals())
#
# print(gallery3.getAllExternals())
#
# print(gallery3.getUnavailableExternals())


# #Initialise available resources
#
# availableProcs = []
# linesIn = []
# linesOut = []
#
# for item in processors:
#     availableProcs.append(Processor(item))
#
# for item in incomingLines:
#     linesIn.append(IncomingLine(item))
#
# for item in outgoingLines:
#     linesOut.append(OutgoingLine(item))
#
#
# matchDate = raw_input('Matchday Date ')
# matchDayInstance = MatchDay(matchDate)
# numberOfMatches = int(raw_input('Number of matches? '))
#
#for match in range(numberOfMatches):
#
#    print '======================'
#    homeTeam = raw_input('Home Team ')
#    awayTeam = raw_input('Away Team ')
#    kickOff = raw_input('Kick Off ')
#    hostBroadcaster = raw_input('Host Broadcaster ')
#    superFeed = raw_input('Superfeed [y/n]? ')
#    miniFeed = raw_input('Minifeed [y/n]? ')
#    comms = ''
#    commsHost = raw_input('Comms from hostbroadcaster [y/n]? ')
#    if commsHost in ('Y', 'y'):
#        comms = 'Host Commentary'
#    else:
#        commsOffTube = raw_input('Comms Off Tube [y/n]? ')
#        if commsOffTube in ('Y', 'y'):
#            comms = 'Off Tube Commentary'
#        else:
#            commsOnSite = raw_input('PLP Comms On Site [y/n]? ')
#            if commsOnSite in ('Y', 'y'):
#                comms = 'Off Tube Commentary'
#
#
#    matchDayInstance.addMatch((Match(homeTeam, awayTeam, kickOffTime, hostBroadcaster, superFeed, comms)))