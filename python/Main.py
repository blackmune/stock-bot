import alpaca_trade_api as tradeapi
from config import apca
from clock import APIClock

#set the api
api = tradeapi.REST(apca["APCA_API_KEY_ID"], apca["APCA_API_SECRET_KEY"], api_version='v2')

account = api.get_account()

api.list_positions()

time = APIClock(api)

#print(time.isActiveMarketHours())#account)

print(time.getNextTradingDay())
pass
"""
Psedo Main Runtime Routine #limit 60 transactions per minute
if active market hours
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
Get timezone # All seriallized according to ISO8601
Set timezone
Get time
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