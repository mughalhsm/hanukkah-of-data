import pandas as pd

orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")
product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")
customers_df = pd.read_csv("noahs-csv/noahs-customers.csv")


orders_df["ordered"] = pd.to_datetime(orders_df["ordered"])
orders_between_period_df = orders_df[
    (orders_df["ordered"] >= "2017-04-04") & (orders_df["ordered"].dt.hour <= 5)
]


pastry_df = product_df[(product_df["sku"].str.contains("BKY"))]


all_pastries_ever_sold = pd.merge(
    pastry_df, orders_item_df, on="sku", how="inner"
)  # 7659


pastries_between_period = pd.merge(
    all_pastries_ever_sold, orders_between_period_df, on="orderid", how="inner"
)


customer_merge_df = pd.merge(
    pastries_between_period, customers_df, on="customerid", how="inner"
)
print(customer_merge_df)

# Drop the "B" and "C" columns from the DataFrame
customer_merge_df = customer_merge_df.drop(
    ["desc", "wholesale_cost", "orderid", "total", "unit_price", "address", "items"],
    axis=1,
)

# Print the resulting DataFrame
# print(customer_merge_df)

name_counts = customer_merge_df["name"].value_counts()

# Sort the dataframe by the name that appears the most in descending order
sorted_df = customer_merge_df.sort_values(
    by="name", key=lambda x: x.map(name_counts), ascending=False
)

# Print the resulting dataframe
print(sorted_df.head(20))

result = sorted_df.iloc[0]
print(result)


# customer_merge_df['birthdate'] = pd.to_datetime(customer_merge_df['birthdate'])

# sorted_df = customer_merge_df.sort_values(by='birthdate', ascending=False)

# print(sorted_df)
