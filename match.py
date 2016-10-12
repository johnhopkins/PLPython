class Match(object):
    
    def __init__(self, homeTeam, awayTeam, kickOff, hostBroadcaster, superFeed, miniFeed, comms):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.kickOffTime = kickOffTime
        self.hostBroadcaster = hostBroadcaster
        self.comms = comms

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getKickOff(self):
        return self.kickOff

    def __str__(self):
        return (self.homeTeam + ' v ' + self.awayTeam)
