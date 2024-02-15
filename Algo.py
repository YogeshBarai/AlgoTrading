from DataLoader import DataLoader
from TrendFollowingStrategy import TrendFollowingStrategy
from MeanReversionStrategy import MeanReversionStrategy
import os

# Function to create output folder if it doesn't exist
def create_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# Function to process a single file
def process_file(file_path, output_folder):
    # Load data
    data = DataLoader.load_data(file_path)

    # Initialize strategy classes
    trend_following_strategy = TrendFollowingStrategy(data)
    mean_reversion_strategy = MeanReversionStrategy(data)

    # Generate signals
    signals_trend = trend_following_strategy.generate_signals()
    signals_mean_reversion = mean_reversion_strategy.generate_signals()
    
    # Output file name
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Save signals to CSV files
    output_trend_path = os.path.join(output_folder, file_name + '_TFS.csv')
    output_mean_reversion_path = os.path.join(output_folder, file_name + '_MRS.csv')
    signals_trend.to_csv(output_trend_path)
    signals_mean_reversion.to_csv(output_mean_reversion_path)

    print(f"Trend-following signals saved to {output_trend_path}")
    print(f"Mean reversion signals saved to {output_mean_reversion_path}")

# Process all CSV files in input folder
input_folder = 'historical_data'
output_folder = 'output'

# Create output folder if it doesn't exist
create_output_folder(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_folder, file_name)
        process_file(file_path, output_folder)
