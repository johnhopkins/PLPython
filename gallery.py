class Gallery(object):
    def __init__(self):
        self.tx = {'TX1': False, 'TX2':False}
        self.externals = {'EXT1': False, 'EXT2':False}

    def getAllExternals(self):
        return self.externals

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

class Gallery1(Gallery):
    def __init__(self):
        self.tx = {'TX1': False, 'TX2':False}
        self.externals = {'EXT1': True, 'EXT2':False, 'EXT3': False, 'EXT4': False, 'EXT5': False}
