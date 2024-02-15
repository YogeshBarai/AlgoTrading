# Algorithmic Trading Strategy Implementation

This repository contains Python code demonstrating the implementation of algorithmic trading strategies using a modular class-based approach. The code is organized into separate classes and files for loading data, implementing trading strategies, and running the main application.

## Files

- `DataLoader.py`: Contains the `DataLoader` class responsible for loading historical price data from a CSV file.
- `TrendFollowingStrategy.py`: Implements the `TrendFollowingStrategy` class for a trend-following trading strategy.
- `MeanReversionStrategy.py`: Implements the `MeanReversionStrategy` class for a mean reversion trading strategy.
- `Algo.py`: Main application script for loading data, instantiating strategy objects, and generating trading signals.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Place your historical price data in a CSV file.  (e.g., `AAPL.csv`).
4. Update the file path in `Algo.py` to point to your CSV file. Currently the input folder is called as "historical_data"
5. Run the `Algo.py` script to generate trading signals based on the implemented strategies.

## Strategy Details

- **Trend-Following Strategy:** Generates buy signals when the short-term moving average crosses above the long-term moving average, and sell signals when the opposite occurs.
- **Mean Reversion Strategy:** Generates buy signals when the current price is below a certain threshold (rolling mean minus rolling standard deviation), and sell signals when the price is above the threshold.

## Output

The generated trading signals are displayed in the console output of `Algo.py`.

## Disclaimer

This code is provided for educational purposes only and should not be considered financial advice. Algorithmic trading involves risks, and the strategies implemented here may not be suitable for all trading scenarios. Always conduct thorough testing and analysis before deploying any trading strategy in live markets.
