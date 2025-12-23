from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import random
from expense_tracker.api.expense_api import ExpenseAPI

def _generate_expense(_):
    return (
        round(random.uniform(10, 200), 2),
        random.choice(["Food", "Transport", "Utilities"]),
        "Generated expense",
        "2025-01-01"
    )

def initialize_database(n=3000):
    with Pool() as pool:
        expenses = pool.map(_generate_expense, range(n))

    api = ExpenseAPI()

    with ThreadPoolExecutor() as executor:
        executor.map(lambda e: api.add_expense(*e), expenses)


if __name__ == "__main__":
    initialize_database()
