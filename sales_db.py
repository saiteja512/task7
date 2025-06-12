import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

cursor.execute('SELECT COUNT(*) FROM sales')
if cursor.fetchone()[0] == 0:
    sample_data = [
        ('Apple', 10, 0.5),
        ('Banana', 5, 0.3),
        ('Orange', 8, 0.7),
        ('Apple', 15, 0.5),
        ('Banana', 10, 0.3)
    ]
    cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
    conn.commit()

query = '''
    SELECT product,
           SUM(quantity) AS total_qty,
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
'''
df = pd.read_sql_query(query, conn)

print("Sales Summary:")
print(df)

df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()


conn.close()
