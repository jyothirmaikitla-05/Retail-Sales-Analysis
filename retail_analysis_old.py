import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset/Superstore.csv", encoding="latin1")

# Fill Missing Values
df["Postal Code"] = df["Postal Code"].fillna(df["Postal Code"].mode()[0])

# ==========================
# BASIC SALES ANALYSIS
# ==========================

print("========== BASIC SALES ANALYSIS ==========")
print("Total Sales :", round(df["Sales"].sum(), 2))
print("Total Profit :", round(df["Profit"].sum(), 2))
print("Average Sales :", round(df["Sales"].mean(), 2))
print("Highest Sale :", df["Sales"].max())
print("Lowest Sale :", df["Sales"].min())

# ==========================
# CATEGORY WISE SALES
# ==========================

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/category_sales.png")
plt.show()

# ==========================
# REGION WISE SALES
# ==========================

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\n========== REGION WISE SALES ==========")
print(region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/region_sales.png")
plt.show()


# TOP 10 STATES
# ======

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

print("\n========== TOP 10 STATES ==========")
print(state_sales)

plt.figure(figsize=(10,5))
state_sales.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/top10_states.png")
plt.show()

# MONTHLY SALES ANALYSIS


# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Month-Year column
df["Month"] = df["Order Date"].dt.to_period("M")

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# Plot
plt.figure(figsize=(12,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/monthly_sales.png")

plt.show()
# ==========================
# TOP 10 PRODUCTS BY SALES
# ==========================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_products)

plt.figure(figsize=(12,6))
top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.xticks(rotation=75, ha="right")

plt.tight_layout()

plt.savefig("images/top10_products.png")

plt.show()
# ==========================
# CUSTOMER SEGMENT ANALYSIS
# ==========================

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

print("\n========== CUSTOMER SEGMENT SALES ==========")
print(segment_sales)

plt.figure(figsize=(7,5))
segment_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales by Customer Segment")
plt.ylabel("")

plt.tight_layout()

plt.savefig("images/customer_segment.png")

plt.show()
# ==========================
# PROFIT ANALYSIS
# ==========================

state_profit = df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(10)

print("\n========== TOP 10 STATES BY PROFIT ==========")
print(state_profit)

plt.figure(figsize=(10,5))
state_profit.plot(kind="bar")

plt.title("Top 10 States by Profit")
plt.xlabel("State")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/top10_profit_states.png")

plt.show()
# ==========================
# SHIP MODE ANALYSIS
# ==========================

ship_mode = df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)

print("\n========== SHIP MODE SALES ==========")
print(ship_mode)

plt.figure(figsize=(7,5))
ship_mode.plot(kind="bar")

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/ship_mode_sales.png")

plt.show()
# ==========================
# TOP 10 CUSTOMERS
# ==========================

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\n========== TOP 10 CUSTOMERS ==========")
print(top_customers)

plt.figure(figsize=(10,5))
top_customers.plot(kind="bar")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Sales")

plt.xticks(rotation=75, ha="right")

plt.tight_layout()

plt.savefig("images/top10_customers.png")

plt.show()


# ==========================
# DISCOUNT VS PROFIT
# ==========================

plt.figure(figsize=(8,5))

plt.scatter(df["Discount"], df["Profit"])

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/discount_vs_profit.png")

plt.show()


# ==========================
# SALES BY YEAR
# ==========================

df["Year"] = df["Order Date"].dt.year

year_sales = df.groupby("Year")["Sales"].sum()

print("\n========== SALES BY YEAR ==========")
print(year_sales)

plt.figure(figsize=(7,5))

year_sales.plot(kind="bar")

plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/sales_by_year.png")

plt.show()