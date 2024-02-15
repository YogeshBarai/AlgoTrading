import pandas as pd

class MeanReversionStrategy:
    def __init__(self, data):
        self.data = data

    def generate_signals(self, window=20):
        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['Close']

        signals['rolling_mean'] = self.data['Close'].rolling(window=window).mean()
        signals['rolling_std'] = self.data['Close'].rolling(window=window).std()

        signals['z_score'] = (self.data['Close'] - signals['rolling_mean']) / signals['rolling_std']

        # Generate buy/sell signals based on z-score
        signals['signal'] = 0
        signals['signal'][signals['z_score'] < -1] = 1  # Buy signal
        signals['signal'][signals['z_score'] > 1] = -1   # Sell signal

        return signals
