from match import *
from gallery import *
from matchday import *
from data import *
from tielines import *
from feed import *
from plan import *

a = Feed('Clean', Plan('002'), Tieline())
b = Feed('Backup Clean', Plan('082'), Tieline())
c = Feed('Wide', Plan('004'), Tieline())

print(a.name)
print(a.tieline.tielineNumber())
print(a.incomingline.number)

print(b.name)
print(b.tieline.tielineNumber())
print(b.incomingline.number)

print(c.name)
print(c.tieline.tielineNumber())
print(c.incomingline.number)

print(Tieline.availableTielines)

# gallery3 = Gallery()
#
# print(gallery3.getAvailableExternals())
#
# print(gallery3.getAllExternals())
#
# print(gallery3.getUnavailableExternals())


'''All the following to be webified!'''
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