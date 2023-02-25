import pandas as pd

from customer_processor import CustomerProcessor

processor = CustomerProcessor("noahs-csv/noahs-customers.csv")

processor.df["Initials"] = processor.df["name"].apply(
    lambda x: "".join([name[0] for name in x.split()])
)

result = processor.df[processor.df["Initials"] == "JD"]

print(result)


product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")

coffee_or_bagel_rows = product_df[product_df["desc"].str.contains("Coffee|Bagel")]


merged_df = pd.merge(coffee_or_bagel_rows, orders_item_df, on="sku", how="inner")

sku_values_to_keep = ["DLI1464", "BKY5887", "BKY4234"]

filtered_df = merged_df[merged_df["sku"].isin(sku_values_to_keep)]


merged_df_2 = pd.merge(filtered_df, orders_df, on="orderid", how="inner")

merged_df_2["ordered"] = pd.to_datetime(merged_df_2["ordered"])

# Extract the year component from the "ordered" column
merged_df_2["year"] = merged_df_2["ordered"].dt.year

# Filter the dataframe to include only the rows where the year is 2017
filtered_df_2 = merged_df_2[merged_df_2["year"] == 2017]

# Print the resulting dataframe
merged_df_3 = pd.merge(result, filtered_df_2, on="customerid", how="inner")

print(merged_df_3)
