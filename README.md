# SQL Sales Analysis with SQLite and Python

## Project Overview

This project demonstrates how to perform data analysis using **SQL queries on a local SQLite database** and automate the process using Python.

The dataset is imported from a CSV file into a SQLite database. Then, several SQL queries are executed using Python to extract insights about sales performance, product categories, and regional trends.

The results of each query are automatically exported as CSV files for further analysis or visualization.

---

## Tools Used

* Python
* SQL
* SQLite
* Pandas

---

## Dataset

The dataset contains retail sales transactions including:

* Orders
* Customers
* Products
* Sales
* Profit
* Discounts
* Regions

Main columns include:

* Order Date
* Category
* Sub-Category
* Product Name
* Sales
* Profit
* Region

---

## Project Structure

sql-sales-analysis

data
└── sales.csv

database
└── sales.db

queries
└── sales_analysis.sql

scripts
├── create_database.py
└── run_queries.py

results
├── total_sales.csv
├── sales_by_category.csv
├── sales_by_region.csv
├── top_products.csv
└── profit_by_category.csv

README.md

---

## Step 1 – Clone the Repository

git clone https://github.com/dbelenmarinflores/sql-sales-analysis.git

cd sql-sales-analysis

---

## Step 2 – Create the Database

Run the script to create the SQLite database and import the dataset:

python scripts/create_database.py

This script will:

* Read the CSV dataset
* Create a SQLite database
* Generate a table called **sales**

The database file will be created here:

database/sales.db

---

## Step 3 – Run SQL Analysis

Execute the SQL queries automatically with Python:

python scripts/run_queries.py

The script will:

* Connect to the SQLite database
* Execute several SQL queries
* Export each result as a CSV file

---

## Results

The results of each analysis will be stored in the **results** folder.

Examples:

Total Sales
results/total_sales.csv

Sales by Category
results/sales_by_category.csv

Sales by Region
results/sales_by_region.csv

Top Products
results/top_products.csv

Profit by Category
results/profit_by_category.csv

---

## Example SQL Query

Sales by Category

SELECT Category, SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

---

## Insights Generated

The analysis allows us to identify:

* Which product categories generate the highest sales
* Regional sales performance
* Top selling products
* Profit distribution by category

These insights can support business decision-making and performance evaluation.

---

## Author

Deborah Belen Marin Flores

GitHub
https://github.com/dbelenmarinflores