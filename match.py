class Match(object):
    
    def __init__(self):
        self.homeTeam = None
        self.awayTeam = None
        self.kickOffTime = None
        self.hostBroadcaster = None
        self.comms = None
        self.level = None
        self.gallery = None

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getKickOff(self):
        return self.kickOffTime

    def getHostBroadcaster(self):
        return self.hostBroadcaster

    def getCommentary(self):
        return self.comms

    def level(self):
        return self.level

    def __str__(self):
        return (self.homeTeam + ' v ' + self.awayTeam)