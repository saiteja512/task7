# Sales Summary from SQLite with Python

## 📌 Overview
This project demonstrates how to use **SQLite** and **Python** to:
- Query a small sales database
- Calculate total quantity sold and revenue per product
- Display results using `print()` and a basic **matplotlib** bar chart

## 🛠 Tools Used
- Python 3.x
- SQLite (built-in via `sqlite3`)
- Pandas
- Matplotlib

## 📂 Files
- `sales_summary.py` — Main script that:
  - Connects to `sales_data.db`
  - Creates a sample `sales` table (if not present)
  - Executes SQL queries to summarize data
  - Plots a revenue bar chart (`sales_chart.png`)

## ▶️ How to Run
1. Make sure you have Python installed.
2. Install required libraries:
3. Run the script:
4. View the output in the console and the generated bar chart.

## 📊 Output
- Printed sales summary in terminal
- A bar chart image: `sales_chart.png`

## ✅ Example Output

| product | total_qty | revenue |
|---------|-----------|---------|
| Apple   |    25     |  12.5   |
| Banana  |    15     |   4.5   |
| Orange  |     8     |   5.6   |

---


