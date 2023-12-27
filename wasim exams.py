
import numpy as np
import talib
import time

# Alpaca API credentials
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'  # For paper trading
APCA_API_KEY_ID = 'PKNYOBDZTWSUGWG0AROB'
APCA_API_SECRET_KEY = '9Xcf5MEpRbLj3PSPTT8bfFze8JWTHbQCQsz5kRk1'

import alpaca_trade_api as tradeapi
import pandas as pd
from alpaca_trade_api.rest import TimeFrame

api = tradeapi.REST(
    key_id=APCA_API_KEY_ID,
    secret_key=APCA_API_SECRET_KEY,
    base_url="https://paper-api.alpaca.markets"
)



import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import talib



# Initialize Alpaca API

# Define stock symbol and timeframe
symbol = 'AAPL'
timeframe = 'day'  # 'minute', 'hour', 'day'

# Get historical data
data = api.get_bars("AAPL", TimeFrame.Hour, "2023-08-22", "2023-08-26")
bars = data

# Create a DataFrame with the historical data
df = pd.DataFrame(columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
t = 0
for bar in bars:


    df = df.append({'timestamp': bar.t, 'open': bar.o, 'high': bar.h, 'low': bar.l, 'close': bar.c, 'volume': bar.v}, ignore_index=True)

# Calculate indicators
df['short_mavg'] = df['close'].rolling(window=10).mean()
df['long_mavg'] = df['close'].rolling(window=50).mean()
df['rsi'] = talib.RSI(df['close'], timeperiod=14)

# Initialize variables
capital = 10000  # Initial capital
position_size = capital / df['close'].iloc[0]  # Position size for initial entry
print(position_size)
positions = []

# Implement the trading strategy



apital = 10000  # Initial capital
position_size = capital / 100  # Position size for initial entry

positions = []

# Main trading loop
while True:
    # Get historical data
    bars = api.get_bars("AAPL", TimeFrame.Hour, "2023-06-08", "2023-06-08", adjustment='raw')

    # Create a DataFrame with the historical data
    data = {
        'timestamp': [bar.t for bar in bars],
        'open': [bar.o for bar in bars],
        'high': [bar.h for bar in bars],
        'low': [bar.l for bar in bars],
        'close': [bar.c for bar in bars],
        'volume': [bar.v for bar in bars]
    }
    df = pd.DataFrame(data)

    # Calculate Bollinger Bands
    df['middle_band'] = df['close'].rolling(window=20).mean()

    # Check for trading signals
    if df['close'].iloc[-1] < df['lower_band'].iloc[-1] and len(positions) == 0:
        positions.append('BUY')
        api.submit_order(
            symbol=symbol,
            qty=int(position_size),
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print("Buying")
    elif df['close'].iloc[-1] > df['middle_band'].iloc[-1] and len(positions) > 0:
        positions.pop()
        api.submit_order(
            symbol=symbol,
            qty=int(position_size),
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print("Selling")

    # Wait for a specified interval before checking data again
    time.sleep(60)  # Wait for 1 minute