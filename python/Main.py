import alpaca_trade_api as tradeapi
from config import vars

#set the api
api = tradeapi.REST(vars["APCA_API_KEY_ID"], vars["APCA_API_SECRET_KEY"], api_version='v2')

account = api.get_account()

api.list_positions

print(account)