import logging
from datetime import datetime
from src.database.db import Database
from src.models.expense import Expense

logging.basicConfig(level=logging.INFO)

class ExpenseAPI:
    def __init__(self):
        self.db = Database()

    def add_expense(self, amount, category, description, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        self.db.execute(
            "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
            (amount, category, description, date)
        )

    def get_all_expenses(self):
        rows = self.db.execute("SELECT * FROM expenses").fetchall()
        return [Expense(r[1], r[2], r[3], r[4], r[0]) for r in rows]

    def filter_by_category(self, category):
        rows = self.db.execute(
            "SELECT * FROM expenses WHERE category=?", (category,)
        ).fetchall()
        return [Expense(r[1], r[2], r[3], r[4], r[0]) for r in rows]

    def statistics(self):
        total = self.db.execute(
            "SELECT SUM(amount) FROM expenses"
        ).fetchone()[0]
        return {"total": total or 0}

    def get_expenses_by_date_range(self, start_date, end_date): # new function
        rows = self.db.execute(
            """
            SELECT * FROM expenses
            WHERE date BETWEEN ? AND ?
            """,
            (start_date, end_date)
        ).fetchall()
        return [Expense(r[1], r[2], r[3], r[4], r[0]) for r in rows]

    def category_summary(self): # new function
        rows = self.db.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses
            GROUP BY category
            """
        ).fetchall()
        return {category: total for category, total in rows}