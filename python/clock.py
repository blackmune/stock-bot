from datetime import date
class APIClock:
    today = date.today()
    def __init__(self, api):
        self.api = api
    def isActiveMarketHours(self):
        clock = self.api.get_clock()
        return clock.is_open
    def getNextTradingDay(self):
        calendar = self.api.get_calendar(self.today)

        return calendar

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