# STEP 0: Create a sample sales dataset
# Run this file ONCE. It makes a file called sales_data.csv
# (If you download a real dataset from Kaggle, you can skip this file.)

import pandas  as pd
import random

random.seed(42)  # makes the random numbers the same every time

# Lists of possible values
regions = ["North", "South", "East", "West"]
categories = {
    "Electronics": ["Laptop", "Mobile", "Headphones", "Smartwatch"],
    "Furniture": ["Chair", "Table", "Bookshelf", "Sofa"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Shoes"],
    "Stationery": ["Notebook", "Pen Set", "Backpack", "Calculator"],
}
prices = {
    "Laptop": 55000, "Mobile": 20000, "Headphones": 2500, "Smartwatch": 6000,
    "Chair": 3500, "Table": 7000, "Bookshelf": 5000, "Sofa": 25000,
    "T-Shirt": 600, "Jeans": 1500, "Jacket": 3000, "Shoes": 2500,
    "Notebook": 80, "Pen Set": 250, "Backpack": 1200, "Calculator": 700,
}
customers = ["Customer_" + str(i) for i in range(1, 51)]  # 50 customers

rows = []
for order_id in range(1, 1001):  # 1000 orders
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    quantity = random.randint(1, 5)
    discount = random.choice([0, 0, 0.05, 0.10, 0.20])
    price = prices[product]
    sales = price * quantity * (1 - discount)
    profit = sales * random.uniform(0.05, 0.30)

    # Higher discount can reduce profit (just to make the data interesting)
    if discount == 0.20:
        profit = sales * random.uniform(-0.05, 0.10)

    # Random date in 2023 and 2024
    year = random.choice([2023, 2024])
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)

    rows.append([order_id, date, random.choice(customers), random.choice(regions),
                 category, product, quantity, price, discount,
                 round(sales, 2), round(profit, 2)])

columns = ["Order_ID", "Order_Date", "Customer", "Region", "Category",
           "Product", "Quantity", "Price", "Discount", "Sales", "Profit"]

df = pd.DataFrame(rows, columns=columns)
df.to_csv("sales_data.csv", index=False)
print("sales_data.csv created with", len(df), "rows")
