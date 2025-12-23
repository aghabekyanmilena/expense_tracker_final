import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.execute("SELECT * FROM expenses")

print("id | amount | category | description | date")
print("-" * 50)

for row in cursor.fetchall():
    print(row)

conn.close()
