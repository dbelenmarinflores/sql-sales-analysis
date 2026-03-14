import pandas as pd
import sqlite3

# leer dataset
df = pd.read_csv("data/sales.csv", encoding="latin1")

# conectar base de datos
conn = sqlite3.connect("database/sales.db")

# guardar tabla
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully")

conn.close()