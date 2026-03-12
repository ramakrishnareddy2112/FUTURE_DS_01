import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show first rows
print("First 5 rows of dataset:")
print(df.head())

# Total Revenue
total_revenue = df["Sales"].sum()
print("\nTotal Revenue:", total_revenue)

# Top Selling Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop Selling Products:")
print(top_products)

# Category Sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)

# Regional Sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# Visualization

# Sales by Category
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.savefig("category_sales.png")
plt.close()


# Sales by Region
plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.savefig("region_sales.png")
plt.close()


# Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.close()