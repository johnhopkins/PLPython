class Tieline(object):
    #These are class variables used to keep an overview of which tielines
    #have been allocated and which ones haven't
    availableTielines = []
    for i in range(1,101):
        availableTielines.append(i)
    unavailableTielines = []

    @classmethod
    def getUnavailableTielines(self):
        '''returns a list of unavailable tielines'''
        return self.unavailableTielines

    @classmethod
    def getAvailableTielines(self):
        '''returns a list of available tielines'''
        return self.availableTielines

    def __init__(self):
        self.tieline = Tieline.availableTielines.pop(0)
        Tieline.unavailableTielines.append(self.tieline)

    def tielineNumber(self):
        '''returns the individual tieline number of the instance'''
        return self.tieline

