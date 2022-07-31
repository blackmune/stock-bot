from datetime import date
class APIClock:
    ## TODO: time functions
    # today
    def __init__(self, api):
        self.api = api
        self.clock = self.api.get_clock()
    # now
    # isActiveMarketHours() | returns bool
    def isActiveMarketHours(self):
        return self.clock.is_open
    # next market open
    def getNextOpen(self):
        return self.clock.next_open
    # next market close
    def getNextClose(self):
        return self.clock.next_close
    # is now between market open and market close

"""    
clock = api.get_clock()

date = '2020-7-01'
calendar = api.get_calendar(start=date, end=date)[0]
print('The market opened at {} and closed at {} on {}.'.format(
    calendar.open,
    calendar.close,
    date
))
"""
