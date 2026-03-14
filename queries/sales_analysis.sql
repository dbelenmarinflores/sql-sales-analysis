-- total sales
SELECT SUM(Sales) AS total_sales
FROM sales;

-- sales by category
SELECT Category, SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

-- sales by region
SELECT Region, SUM(Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- top 10 products
SELECT "Product Name", SUM(Sales) AS total_sales
FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;

-- total profit by category
SELECT Category, SUM(Profit) AS total_profit
FROM sales
GROUP BY Category;