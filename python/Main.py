import alpaca_trade_api as tradeapi
import requests
import time
from config import apca, finhub
import finnhub

api = tradeapi.REST(apca["APCA_API_KEY_ID"], apca["APCA_API_SECRET_KEY"], api_version='v2')
#clock = APIClock
from Clock import APIClock

## Setup the APIs
finnhub = finnhub.Client(api_key=finhub["FIN_HUB_KEY"])
APICLOCK = APIClock(api)

## TODO: time functions and clock class
# now
now = time.time()
# today
# next market open
nextOpen = APICLOCK.getNextOpen()
# next market close
nextClose = APICLOCK.getNextClose()

# isMarketOpen() | returns bool
print(APICLOCK.isActiveMarketHours())


## TODO: api functions
# #set the apis

# finRes = finnhub.stock_candles('SNDL', 'D', time.time(), startOfDay)
# print(finRes,"\n\n")

# api.get_clock()['is_open']

# print(finnhub.aggregate_indicator('SNDL', 'D'),"\n\n") 

# print(finnhub.company_basic_financials('SNDL', 'margin'),"\n\n")

# account = api.get_account()

# positions = api.list_positions()

## TODO trade functions

pass
## SNDL or LITB
#orderRes = api.submit_order("SNDL", 1, "buy", "limit", "day", ".975", None, None, None, None, None, None, None, None, None)
#print(orderRes)
"""
Psedo Main Runtime Routine #limit 60 transactions per minute
if active market hours else sleep #super inefficient, refactor
    loop through active buys check for acceptable sell price.
        if acceptable sell price
            sell at market value
    if buying power has enough buy threshhold #Assumption buying power is the 'settled cash' # Possibly regt_buying_power
        loop through potential buys
            find best acceptable buy
                if acceptable buy
                    buy threshhold number of stocks
"""

"""
Required Function List:
Get timerzone # All seriallized according to ISO8601
Set timerzone
Get timer
Get Day of the week
Set active days of week
Get active hours start
Get active hours end
is_active_market_hours
Sleep
Set active hours start
Set active hours end
Get buying power
Get threshold
Set threshold
Get active buys
Set active buy # Permanent storage system
Get stock price
Buy # Limit # api.submit_order()
Sell # Limit
list_active_positions() #APIs
find_best_possible_buy
is_acceptable_sell_price(active_buy)
"""

"""
tests:
"""

"""
Edge Cases:
Start of buying day
End of buying day
"""

#REST.get_last_quote("tsla")