import pandas as pd
import sqlite3

# PYTHON ANALYSIS

#Load Dataset
sales = pd.read_csv('superstore.csv', encoding='latin1', index_col=0)

# See first rows
print(sales.head())

#Check columns
print('Sales Columns:', sales.columns)

# Total sales
print('Total Sales:' , sales['Sales'].sum())

#Total Profit
print('Total Profit:', sales['Profit'].sum())

# Sales by Category
print(sales.groupby('Category')['Sales'].sum())

print("----------------------------------------------------------------")
# SQL ANALYSIS

#Create Database
conn = sqlite3.connect('sqlite/sales.db')

#Save data to table
sales.to_sql("Sales", conn, if_exists= "replace", index = False)

cursor = conn.cursor()

print("Data saved to SQLite database")

# Total Sales
cursor.execute("SELECT SUM(Sales) FROM Sales")
print("Total Sales (SQL):", cursor.fetchone()[0])

# Total Profit
cursor.execute("SELECT SUM(Profit) FROM Sales")
print("Total Profit (SQL):", cursor.fetchone()[0])

# Sales by Region
cursor.execute("""
SELECT Region, SUM(Sales)
FROM Sales
GROUP BY Region
""")
sales_by_region = cursor.fetchall()
print("Sales by Region")
for region, total in sales_by_region:
    print(f"{region}: ${total:,.2f}")

print("----------------------------------------------------------------")

# Sales by Category
cursor.execute("""
SELECT Category, SUM(Sales)
FROM Sales
GROUP BY Category
""")
sales_by_category = cursor.fetchall()
print("Sales by Category")
for category, total in sales_by_category:
     print(f"{category}: ${total:,.2f}")

print("----------------------------------------------------------------")

# Top 5 Products by Sales
cursor.execute("""
SELECT "Product Name", SUM(Sales) AS TotalSales
FROM Sales
GROUP BY "Product Name"
ORDER BY TotalSales DESC
LIMIT 5
""")
top_products = cursor.fetchall()
print("Top 5 Products by Sales:")
for product ,total in top_products:
    print(f"{product}:${total:,.2f}")

print(cursor.fetchall())

