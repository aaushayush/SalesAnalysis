# =====================================
#     SALES DATA ANALYSIS (SIMPLE)
# =====================================
# Keep this file in the same folder as sales_data.csv
# Run it with:  python sales_analysis_simple.py

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------
# STEP 1: Read the data
# -------------------------------------
df = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(df.head())

print("Number of rows and columns:")
print(df.shape)

print("Column names:")
print(df.columns)

# -------------------------------------
# STEP 2: Clean the data
# -------------------------------------
# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows that have missing values
df = df.dropna()

# Change the date column from text to real date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Make two new columns: Year and Month
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month

# -------------------------------------
# STEP 3: Total numbers
# -------------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_sale = df["Sales"].mean()

print("Total Sales =", total_sales)
print("Total Profit =", total_profit)
print("Total Orders =", total_orders)
print("Average Sale =", average_sale)

# -------------------------------------
# STEP 4: Analysis
# -------------------------------------
# groupby means: "make groups, then add up each group"
# Example: sales of each Category added together

# 4.1 Sales of each year
year_sales = df.groupby("Year")["Sales"].sum()
print("Sales of each year:")
print(year_sales)

# 4.2 Sales of each month
month_sales = df.groupby("Month")["Sales"].sum()
print("Sales of each month:")
print(month_sales)

# 4.3 Sales of each category
category_sales = df.groupby("Category")["Sales"].sum()
print("Sales of each category:")
print(category_sales)

# 4.4 Sales of each product
product_sales = df.groupby("Product")["Sales"].sum()
product_sales = product_sales.sort_values(ascending=False)
top_products = product_sales.head(5)
print("Top 5 products:")
print(top_products)

# 4.5 Sales of each region
region_sales = df.groupby("Region")["Sales"].sum()
print("Sales of each region:")
print(region_sales)

# 4.6 Profit of each category
category_profit = df.groupby("Category")["Profit"].sum()
print("Profit of each category:")
print(category_profit)

# 4.7 Average profit for each discount
discount_profit = df.groupby("Discount")["Profit"].mean()
print("Average profit for each discount:")
print(discount_profit)

# -------------------------------------
# STEP 5: Charts
# -------------------------------------

# Chart 1: Sales of each year
year_sales.plot(kind="bar")
plt.title("Sales of Each Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.savefig("chart1_year_sales.png")
plt.close()

# Chart 2: Sales of each month (line chart)
month_sales.plot(kind="line")
plt.title("Sales of Each Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("chart2_month_sales.png")
plt.close()

# Chart 3: Sales of each category (pie chart)
category_sales.plot(kind="pie")
plt.title("Sales by Category")
plt.ylabel("")
plt.savefig("chart3_category_sales.png")
plt.close()

# Chart 4: Top 5 products
top_products.plot(kind="bar")
plt.title("Top 5 Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("chart4_top_products.png")
plt.close()

# Chart 5: Sales of each region
region_sales.plot(kind="bar")
plt.title("Sales of Each Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("chart5_region_sales.png")
plt.close()

# Chart 6: Profit of each category
category_profit.plot(kind="bar")
plt.title("Profit of Each Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.savefig("chart6_category_profit.png")
plt.close()

# Chart 7: Discount and profit
discount_profit.plot(kind="bar")
plt.title("Average Profit for Each Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.savefig("chart7_discount_profit.png")
plt.close()

# -------------------------------------
# STEP 6: Conclusion
# -------------------------------------
print("========== CONCLUSION ==========")
print("Best category :", category_sales.idxmax())
print("Best product  :", product_sales.idxmax())
print("Best region   :", region_sales.idxmax())
print("Best month    :", month_sales.idxmax())
print("Higher discount gives less profit (see chart 7).")
