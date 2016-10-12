class MatchDay(object):
    def __init__(self, date):
        self.date = date
        self.matches = []

    def getDate(self):
        return self.date

    def addMatch(self, matchObject):
        self.matches.append(matchObject)
