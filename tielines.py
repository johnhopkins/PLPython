class Tieline(object):

    #This is a class variable used to keep track of how many tielines have been allocated.
    totalTielinesUsed = 0

    def __init__(self):
        Tieline.totalTielinesUsed +=1
        self.tieline = Tieline.totalTielinesUsed

    def tielineNumber(self):
        return self.tieline

    def howMany(self):
        return self.totalTielinesUsed



