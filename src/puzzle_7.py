import pandas as pd

customers_df = pd.read_csv("noahs-csv/noahs-customers.csv")

product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")
orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")


df = pd.merge(orders_item_df, orders_df, on="orderid", how="inner")
df = pd.merge(df, customers_df, on="customerid", how="inner")
df = pd.merge(df, product_df, on="sku", how="inner")
df = df.drop(
    [
        "unit_price",
        "sku",
        "qty",
        "address",
        "birthdate",
        "wholesale_cost",
        "citystatezip",
        "total",
        "shipped",
        "items",
    ],
    axis=1,
)
df = df.sort_values("orderid", ascending=True)
emily_mask = df["customerid"] == 8342
emily_mask_next = emily_mask.shift(1, fill_value=False)
emily_and_next_mask = emily_mask | emily_mask_next


df = df[emily_and_next_mask]
df = df[df["desc"].str.contains("[()]")]
df["product"] = df["desc"].str.extract(r"^(.+?)(?=\s*\()")
df = df.groupby("product").filter(lambda x: len(x["name"].unique()) > 1)
result = df[df["customerid"] != 8342]


print(result)
