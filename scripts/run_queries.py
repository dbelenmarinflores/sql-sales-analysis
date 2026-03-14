import sqlite3
import pandas as pd
import os

# conectar base de datos
conn = sqlite3.connect("database/sales.db")

# crear carpeta resultados si no existe
os.makedirs("results", exist_ok=True)

queries = {

    "total_sales": """
    SELECT SUM(Sales) AS total_sales
    FROM sales
    """,

    "sales_by_category": """
    SELECT Category, SUM(Sales) AS total_sales
    FROM sales
    GROUP BY Category
    ORDER BY total_sales DESC
    """,

    "sales_by_region": """
    SELECT Region, SUM(Sales) AS total_sales
    FROM sales
    GROUP BY Region
    ORDER BY total_sales DESC
    """,

    "top_products": """
    SELECT "Product Name", SUM(Sales) AS total_sales
    FROM sales
    GROUP BY "Product Name"
    ORDER BY total_sales DESC
    LIMIT 10
    """,

    "profit_by_category": """
    SELECT Category, SUM(Profit) AS total_profit
    FROM sales
    GROUP BY Category
    ORDER BY total_profit DESC
    """
}

# ejecutar consultas
for name, query in queries.items():

    df = pd.read_sql(query, conn)

    output_path = f"results/{name}.csv"

    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")

conn.close()