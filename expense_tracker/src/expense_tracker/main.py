from expense_tracker.api.expense_api import ExpenseAPI
from expense_tracker.models.expense import Expense
from datetime import datetime

def main():
    api = ExpenseAPI()

    try:
        while True:
            print("\nWelcome to your Expense Tracker!")
            print("1. Add expense")
            print("2. View all expenses")
            print("3. View statistics")
            print("4. Exit")

            choice = input("> ").strip()

            if choice == "1":
                while True:
                    try:
                        amount = float(input("Enter amount: "))
                        if amount < 0:
                            print("Amount can't be negative!")
                            continue
                        break
                    except ValueError:
                        print("Invalid amount! Please enter a number.")

                category = input("Enter category: ").strip()
                description = input("Enter description: ").strip()
                date_input = input("Enter date (YYYY-MM-DD) [optional]: ").strip()
                date = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

                existing = api.filter_by_category(category)
                duplicate = any(
                    e.amount == amount and e.description == description and e.date == date
                    for e in existing
                )

                if duplicate:
                    print("Duplicate expense detected! Not added.")
                else:
                    api.add_expense(amount, category, description, date)
                    print("Expense added successfully!")

            elif choice == "2":
                expenses = api.get_all_expenses()
                if not expenses:
                    print("No expenses yet.")
                else:
                    for e in expenses:
                        print(e)

            elif choice == "3":
                stats = api.statistics()
                print(f"Total spent: {stats['total']}")

            elif choice == "4":
                print("Exiting program. All data is already saved to DB.")
                break

            else:
                print("Invalid choice, try again.")

    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted. All entered data is saved to DB.!")


if __name__ == "__main__":
    main()
