import pandas as pd


class CustomerProcessor:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def add_last_name_column(self):
        self.df["lastname"] = self.df["name"].str.split().str[-1]
