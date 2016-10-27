class Round(object):

    def __init__(self, matchround):
        self.matchRound = matchround
        self.matchdays = []

    def addmatchday(self, matchday):
        self.matchdays.append(matchday)

    def getmatchround(self):
        return self.matchRound

    def getnumberofmatchdays(self):
        return len(self.matchdays)

    def getallmatchdays(self):
        return self.matchdays