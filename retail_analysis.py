import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# LOAD DATA
# ==========================================

def load_data():

    df = pd.read_csv("dataset/Superstore.csv", encoding="latin1")

    df["Postal Code"] = df["Postal Code"].fillna(
        df["Postal Code"].mode()[0]
    )

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    df["Month"] = df["Order Date"].dt.to_period("M")

    df["Year"] = df["Order Date"].dt.year

    return df


# ==========================================
# BASIC SALES ANALYSIS
# ==========================================

def basic_sales_analysis(df):

    print("\n========== BASIC SALES ANALYSIS ==========\n")

    print(f"Total Sales      : {df['Sales'].sum():,.2f}")
    print(f"Total Profit     : {df['Profit'].sum():,.2f}")
    print(f"Average Sales    : {df['Sales'].mean():,.2f}")
    print(f"Highest Sale     : {df['Sales'].max():,.2f}")
    print(f"Lowest Sale      : {df['Sales'].min():,.2f}")
    print(f"Total Orders     : {df['Order ID'].nunique()}")
    print(f"Total Customers  : {df['Customer ID'].nunique()}")
    print(f"Total Products   : {df['Product Name'].nunique()}")


# ==========================================
# CATEGORY WISE SALES
# ==========================================

def category_analysis(df):

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== CATEGORY WISE SALES ==========\n")
    print(category_sales)

    plt.figure(figsize=(8,5))

    category_sales.plot(kind="bar")

    plt.title("Category Wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("images/category_sales.png")

    plt.show()


# ==========================================
# REGION WISE SALES
# ==========================================

def region_analysis(df):

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== REGION WISE SALES ==========\n")
    print(region_sales)

    plt.figure(figsize=(8,5))

    region_sales.plot(kind="bar")

    plt.title("Region Wise Sales")
    plt.xlabel("Region")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("images/region_sales.png")

    plt.show()


# ==========================================
# TOP 10 STATES
# ==========================================

def state_analysis(df):

    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========== TOP 10 STATES ==========\n")
    print(state_sales)

    plt.figure(figsize=(10,5))

    state_sales.plot(kind="bar")

    plt.title("Top 10 States by Sales")
    plt.xlabel("State")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("images/top10_states.png")

    plt.show()
# ==========================================
# MONTHLY SALES ANALYSIS
# ==========================================

def monthly_sales_analysis(df):

    monthly_sales = df.groupby("Month")["Sales"].sum()

    print("\n========== MONTHLY SALES ==========\n")
    print(monthly_sales)

    plt.figure(figsize=(12,5))

    monthly_sales.plot(kind="line", marker="o")

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("images/monthly_sales.png")

    plt.show()


# ==========================================
# TOP 10 PRODUCTS
# ==========================================

def top_products_analysis(df):

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========== TOP 10 PRODUCTS ==========\n")
    print(top_products)

    plt.figure(figsize=(12,6))

    top_products.plot(kind="bar")

    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product Name")
    plt.ylabel("Sales")

    plt.xticks(rotation=75, ha="right")
    plt.gcf().subplots_adjust(bottom=0.35)
    plt.tight_layout()

    plt.savefig("images/top10_products.png")

    plt.show()


# ==========================================
# CUSTOMER SEGMENT ANALYSIS
# ==========================================

def customer_segment_analysis(df):

    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== CUSTOMER SEGMENT ==========\n")
    print(segment_sales)

    plt.figure(figsize=(7,5))

    segment_sales.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Sales by Customer Segment")
    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("images/customer_segment.png")

    plt.show()


# ==========================================
# TOP 10 STATES BY PROFIT
# ==========================================

def profit_analysis(df):

    state_profit = (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========== TOP 10 STATES BY PROFIT ==========\n")
    print(state_profit)

    plt.figure(figsize=(10,5))

    state_profit.plot(kind="bar")

    plt.title("Top 10 States by Profit")
    plt.xlabel("State")
    plt.ylabel("Profit")

    plt.tight_layout()

    plt.savefig("images/top10_profit_states.png")

    plt.show()


# ==========================================
# SHIP MODE ANALYSIS
# ==========================================

def ship_mode_analysis(df):

    ship_mode = (
        df.groupby("Ship Mode")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== SHIP MODE SALES ==========\n")
    print(ship_mode)

    plt.figure(figsize=(7,5))

    ship_mode.plot(kind="bar")

    plt.title("Sales by Ship Mode")
    plt.xlabel("Ship Mode")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("images/ship_mode_sales.png")

    plt.show()
# ==========================================
# TOP 10 CUSTOMERS
# ==========================================

def top_customers_analysis(df):

    top_customers = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========== TOP 10 CUSTOMERS ==========\n")
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


# ==========================================
# DISCOUNT VS PROFIT
# ==========================================

def discount_profit_analysis(df):

    plt.figure(figsize=(8,5))

    plt.scatter(df["Discount"], df["Profit"])

    plt.title("Discount vs Profit")

    plt.xlabel("Discount")

    plt.ylabel("Profit")

    plt.tight_layout()

    plt.savefig("images/discount_vs_profit.png")

    plt.show()


# ==========================================
# SALES BY YEAR
# ==========================================

def sales_by_year_analysis(df):

    year_sales = df.groupby("Year")["Sales"].sum()

    print("\n========== SALES BY YEAR ==========\n")
    print(year_sales)

    plt.figure(figsize=(7,5))

    year_sales.plot(kind="bar")

    plt.title("Sales by Year")

    plt.xlabel("Year")

    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("images/sales_by_year.png")

    plt.show()

# ==========================================
# PROJECT CONCLUSION
# ==========================================

def project_conclusion():

    print("\n========== PROJECT CONCLUSION ==========\n")
    print("1. Technology category recorded the highest sales.")
    print("2. West region generated the highest revenue.")
    print("3. Sales increased over the years.")
    print("4. Higher discounts generally reduce profit.")
    print("5. Consumer segment contributes the highest sales.")

# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    df = load_data()

    basic_sales_analysis(df)
    category_analysis(df)
    region_analysis(df)
    state_analysis(df)
    monthly_sales_analysis(df)
    top_products_analysis(df)
    customer_segment_analysis(df)
    profit_analysis(df)
    ship_mode_analysis(df)
    top_customers_analysis(df)
    discount_profit_analysis(df)
    sales_by_year_analysis(df)
    project_conclusion()


if __name__ == "__main__":
    main()

