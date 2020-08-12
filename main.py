import alpaca_trade_api as tradeapi

api = tradeapi.REST('PKU6NYH2AU9ISYKH2174', 'RkVCwK4/JYI2hmRp8je3nKxzEnAGB2LTk4jKo0B3', base_url='https://paper-api.alpaca.markets')

# bars = api.get_barset('AAPL', '1D', limit=1)

print( api.get_last_quote('AAPL') )