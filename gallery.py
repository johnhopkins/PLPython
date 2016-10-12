class Gallery(object):
    def __init__(self):
        '''Sets up a dictionary of available connections with False representing no connection'''
        self.tx = {'TX1': False, 'TX2':False, 'TX3': False, 'TX4':False}
        self.externals = {'EXT1': False, 'EXT2':False, 'EXT3': False, 'EXT4':False, 'EXT5': False, 'EXT6':False, 'Ext7': False}

    def getAllExternals(self):
        return self.externals

    def getAvailableExternals(self):
        '''Returns a sorted list of gallery externals that are set to False, i.e. they are available'''
        availableExternals = []
        for external, value in self.externals.iteritems():
            if value == False:
                availableExternals.append(external)
        return sorted(availableExternals)

    def getUnavailableExternals(self):
        '''Returns a sorted list of gallery externals that are set to True, i.e. they are unavailable'''
        unavailableExternals = []
        for external, value in self.externals.iteritems():
            if value == True:
                unavailableExternals.append(external)
        return sorted(unavailableExternals)

    def getAllTxs(self):
        return self.tx

    def getAvailableTxs(self):
        '''Returns a sorted list of gallery txs that are set to False, i.e. they are available'''
        availableTxs = []
        for tx, value in self.tx.iteritems():
            if value == False:
                availableTxs.append(tx)
        return sorted(availableTxs)

    def getUnavailableTxs(self):
        '''Returns a sorted list of gallery txs that are set to True, i.e they are unavailable'''
        unavailableTxs = []
        for tx, value in self.tx.iteritems():
            if value == True:
                unavailableTxs.append(tx)
        return sorted(unavailableTxs)

class Gallery1(Gallery):
    def __init__(self):
        self.tx = {'TX1': False, 'TX2': False, 'TX3': False, 'TX4': False}
        self.externals = {'EXT1': False, 'EXT2': False, 'EXT3': False, 'EXT4': False, 'EXT5': False, 'EXT6': False,
                          'Ext7': False, 'EXT8': False, 'EXT9': False, 'EXT10': False, 'EXT11': False, 'EXT12': False, 'EXT13': False,
                          'Ext14': False, 'EXT15': False, 'EXT16': False}
