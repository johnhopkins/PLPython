class Match(object):
    
    def __init__(self, homeTeam, awayTeam, kickOffTime, hostBroadcaster, superFeed, comms):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.kickOffTime = kickOffTime
        self.hostBroadcaster = hostBroadcaster
        self.comms = comms
        self.superFeed = superFeed

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getKickOff(self):
        return self.kickOff

    def superFeed(self):
        return self.superFeed

    def __str__(self):
        return (self.homeTeam + ' v ' + self.awayTeam)
