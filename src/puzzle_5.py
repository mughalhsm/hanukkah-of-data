import pandas as pd

customers_df = pd.read_csv("noahs-csv/noahs-customers.csv")

product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")
orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")


queens_customers_df = customers_df[
    (customers_df["citystatezip"].str.contains("Queens Village"))
]
cat_products_df = product_df[
    (product_df["sku"].str.contains("PET")) & (product_df["desc"].str.contains("Cat"))
]


print(queens_customers_df)
print(cat_products_df)
print(orders_item_df)

all_cat_products_sold_df = pd.merge(
    cat_products_df, orders_item_df, on="sku", how="inner"
)

all_cat_products_per_order = pd.merge(
    all_cat_products_sold_df, orders_df, on="orderid", how="inner"
)
cat_products_queens_customers = pd.merge(
    all_cat_products_per_order, queens_customers_df, on="customerid", how="inner"
)


name_counts = cat_products_queens_customers["name"].value_counts()

# Sort the dataframe by the name that appears the most in descending order
sorted_df = cat_products_queens_customers.sort_values(
    by="name", key=lambda x: x.map(name_counts), ascending=False
)
result = sorted_df.iloc[0]
print(result)
