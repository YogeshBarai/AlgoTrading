import pandas as pd

class DataLoader:
    @staticmethod
    def load_data(file_path):
        """
        Load historical price data from CSV file.
        """
        return pd.read_csv(file_path)
