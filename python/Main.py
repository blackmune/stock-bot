import alpaca_trade_api as tradeapi
from config import vars

#set the api
api = tradeapi.REST(vars["APCA_API_KEY_ID"], vars["APCA_API_SECRET_KEY"], api_version='v2')

account = api.get_account()

api.list_positions

print(account)

"""
Psedo Main Runtime Routine #limit 60 transactions per minute
if active market hours
    loop through active buys check for acceptable sell price.
        if acceptable sell price
            sell at market value
    if buying power has enough buy threshhold #Assumption buying pawer is the 'settled cash'
        loop through potential buys
            find best acceptable buy
                if acceptable buy
                    buy threshhold number of stocks
"""

"""
Required Function List:
Get timezone
Set timezone
Get time
Get Day of the week
Get active hours start
Get active hours end
sleep
Set active hours start
Set active hours end
Get threshold
Set threshold
Get active buys
Set active buy

"""