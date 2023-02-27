# find sets all unique noahs items

# find who bought all these items

import pandas as pd

customers_df = pd.read_csv("noahs-csv/noahs-customers.csv")

product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")
orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")

noahs_collectables = product_df[product_df["desc"].str.startswith("Noah's")]

orders_combined = pd.merge(orders_item_df, orders_df, on="orderid", how="inner")
orders_combined = orders_combined.drop(
    ["unit_price", "qty", "ordered", "shipped", "items", "total"], axis=1
)

all_order_with_product_and_customer = pd.merge(
    orders_combined, customers_df, on="customerid", how="inner"
)
all_order_with_product_and_customer = all_order_with_product_and_customer.drop(
    ["address", "birthdate"], axis=1
)

print(noahs_collectables)

print(all_order_with_product_and_customer)

all_collectables_sold = pd.merge(
    all_order_with_product_and_customer, noahs_collectables, on="sku", how="inner"
)

counts = all_collectables_sold["name"].value_counts()

# Use the sorted index of the counts to sort the dataframe by the 'name' column in descending order of value counts
all_collectables_sold_sorted = all_collectables_sold.loc[
    all_collectables_sold["name"].isin(counts.index)
].sort_values(by=["name"], key=lambda x: x.map(counts), ascending=False)

result = all_collectables_sold_sorted.iloc[0]
print(result)
