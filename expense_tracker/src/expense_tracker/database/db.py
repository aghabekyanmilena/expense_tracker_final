import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
        self.db_name = db_name
        self._initialize()

    def _initialize(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL
                )
            """)
            conn.commit()

    def execute(self, query, params=()):
        conn = sqlite3.connect(self.db_name, check_same_thread=False)
        cursor = conn.execute(query, params)
        conn.commit()
        return cursor