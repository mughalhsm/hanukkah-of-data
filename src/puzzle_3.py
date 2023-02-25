import pandas as pd

from customer_processor import CustomerProcessor

processor = CustomerProcessor("noahs-csv/noahs-customers.csv")


processor.df = processor.df[
    processor.df["citystatezip"].str.contains("South Ozone Park")
]
processor.df["birthdate"] = pd.to_datetime(processor.df["birthdate"])
processor.df["birthyear"] = processor.df["birthdate"].dt.year
processor.df["birthmonth"] = processor.df["birthdate"].dt.month
processor.df["daybirthmonth"] = processor.df["birthdate"].dt.day

dog_years = [1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]

processor.df = processor.df[processor.df["birthyear"].isin(dog_years)]

print(processor.df)
