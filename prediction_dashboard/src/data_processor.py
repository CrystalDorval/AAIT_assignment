
import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    def inspect_data(self):
        print("Dataset Shape:")
        print(self.df.shape)

        print("\nFirst 5 Rows:")
        print(self.df.head())

        print("\nData Types:")
        print(self.df.dtypes)

        print("\nMissing Values:")
        print(self.df.isnull().sum())

        print("\nSummary Statistics:")
        print(self.df.describe(include="all"))


if __name__ == "__main__":
    processor = DataProcessor("data/data/data_2026-10-05-180443.csv")
    processor.load_data()
    processor.inspect_data()
