import datetime
class APIClock:
    def __init__(self, api):
        self.api = api
    x = 4
    def isActiveMarketHours(self):
        date = datetime.datetime.now()
        calendar = self.api.get_calendar(start=date, end=date)
        return "today"

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