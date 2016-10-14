class Match(object):
    
    def __init__(self, homeTeam, awayTeam, kickOffTime, hostBroadcaster):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.kickOffTime = kickOffTime
        self.hostBroadcaster = hostBroadcaster
        self.comms = 'comms'
        self.level = 'level'
        self.gallery = 'gallery'

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getKickOff(self):
        return self.kickOff

    def getHostBroadcaster(self):
        return self.hostBroadcaster

    def getCommentary(self):
        return self.comms

    def level(self):
        return self.level

    def __str__(self):
        return (self.homeTeam + ' v ' + self.awayTeam)
