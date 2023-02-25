import pandas as pd

customers_df = pd.read_csv("noahs-csv/noahs-customers.csv")

product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")
orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")

print(product_df)
print(orders_item_df)
print(orders_df)
