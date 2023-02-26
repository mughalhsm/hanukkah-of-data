import pandas as pd

customers_df = pd.read_csv("noahs-csv/noahs-customers.csv")

product_df = pd.read_csv("noahs-csv/noahs-products.csv")
orders_item_df = pd.read_csv("noahs-csv/noahs-orders_items.csv")
orders_df = pd.read_csv("noahs-csv/noahs-orders.csv")


all_items_sold = pd.merge(product_df, orders_item_df, on="sku", how="inner")

order_items_at_loss = all_items_sold[
    all_items_sold["wholesale_cost"] >= all_items_sold["unit_price"]
]


items_at_loss_per_order = pd.merge(
    order_items_at_loss, orders_df, on="orderid", how="left"
)


items_at_loss_per_order = pd.merge(
    items_at_loss_per_order, customers_df, on="customerid", how="inner"
)
items_at_loss_per_order = items_at_loss_per_order.drop(
    [
        "desc",
        "ordered",
        "shipped",
        "citystatezip",
        "birthdate",
        "wholesale_cost",
        "address",
        "unit_price",
    ],
    axis=1,
)

sorted_by_person_bought_at_loss = items_at_loss_per_order.sort_values(
    by="name", key=lambda x: x.map(x.value_counts()), ascending=False
)

result = sorted_by_person_bought_at_loss.iloc[0]
print(result)
