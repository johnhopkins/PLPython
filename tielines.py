class Tieline(object):

    #This is a class list variable used to keep track of how many tielines have been allocated.
    availableTielines = []
    for i in range(1,101):
        availableTielines.append(i)

    def __init__(self):
        self.tieline = Tieline.availableTielines.pop(0)

    def tielineNumber(self):
        return self.tieline

    def howMany(self):
        # returns number of tielines being used (not yet implemented)
        return 0

    def returnList(self):
        return self.availableTielines