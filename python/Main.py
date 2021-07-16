import alpaca_trade_api as tradeapi
import requests
import time
from config import apca, finhub
from clock import APIClock
import finnhub

## Setup the APIs
api = tradeapi.REST(apca[0]["APCA_API_KEY_ID"], apca[0]["APCA_API_SECRET_KEY"], api_version='v2')
finnhub = finnhub.Client(api_key=finhub["FIN_HUB_KEY"])


## TODO: time functions
# now
# today
# next market open
# next market close
# isMarketOpen() | returns bool

## TODO: api functions
# #set the apis

# finRes = finnhub.stock_candles('SNDL', 'D', time.time(), startOfDay)
# print(finRes,"\n\n")

<<<<<<< HEAD
# api.get_clock()['is_open']
=======
finRes = finnhub_client.stock_candles('SNDL', 'D', 1590988249, time.time_ns())
print(finRes)
>>>>>>> bd7597071c23758ed7b19e8be66e92efc9c47f0f

# print(finnhub.aggregate_indicator('SNDL', 'D'),"\n\n") 

<<<<<<< HEAD
# print(finnhub.company_basic_financials('SNDL', 'margin'),"\n\n")
=======
# print(finnhub_client.company_basic_financials('SNDL', 'margin'))
>>>>>>> bd7597071c23758ed7b19e8be66e92efc9c47f0f

# account = api.get_account()

# positions = api.list_positions()

<<<<<<< HEAD
## TODO trade functions

timeses = APIClock(api)

print(timeses.isActiveMarketHours())#account)
pass
=======
# timer = APIClock(api)

# print(timer.isActiveMarketHours())#account)
# pass
>>>>>>> bd7597071c23758ed7b19e8be66e92efc9c47f0f
## SNDL or LITB
#orderRes = api.submit_order("SNDL", 1, "buy", "limit", "day", ".975", None, None, None, None, None, None, None, None, None)
#print(orderRes)
"""
<<<<<<< HEAD
Psedo Main Runtime Routine #limit 60 transactions per minute
if active market hours else sleep #super inefficient, refactor
=======
Psedo Main Runtimer Routine #limit 60 transactions per minute
if active market hours else sleep
>>>>>>> bd7597071c23758ed7b19e8be66e92efc9c47f0f
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