import pandas as pd

class TrendFollowingStrategy:
    def __init__(self, data):
        self.data = data

    def generate_signals(self, short_window=20, long_window=50):
        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['Close']

        signals['short_mavg'] = self.data['Close'].rolling(window=short_window, min_periods=1).mean()
        signals['long_mavg'] = self.data['Close'].rolling(window=long_window, min_periods=1).mean()

        signals['signal'] = 0
        signals['signal'][short_window:] = signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:]

        # Generate buy/sell signals
        signals['positions'] = signals['signal'].diff()

        return signals
