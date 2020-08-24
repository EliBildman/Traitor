import alpaca_trade_api as tradeapi
import secret

api = tradeapi.REST(secret.KEY_ID, secret.SECRET_KEY, base_url='https://paper-api.alpaca.markets')

# bars = api.get_barset('AAPL', '1D', limit=1)

print( api.get_last_quote('AAPL') )