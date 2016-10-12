class HDSDI(object):
    def __init__(self):
        self.vision = {'Vision'}
        self.audios = {'EXT1': False, 'EXT2':False}

    def getVision(self):
        return self.vision

    def getAvailableExternals(self):
        '''Returns a sorted list of gallery externals that are not set to False, i.e. they are available'''
        availableExternals = []
        for external, value in self.externals.iteritems():
            if value == False:
                availableExternals.append(external)
        return sorted(availableExternals)

    def getAllTxs(self):
        return self.tx

    def getAvailableTxs(self):
        '''Returns a sorted list of gallery txs that are not set to False, i.e. they are available'''
        availableTxs = []
        for tx, value in self.tx.iteritems():
            if value == False:
                availableTxs.append(tx)
        return sorted(availableTxs)