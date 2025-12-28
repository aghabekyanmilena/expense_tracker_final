from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date=None, expense_id=None):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self._id = expense_id
        self._amount = amount
        self._category = category
        self._description = description
        self._date = date or datetime.now().strftime("%Y-%m-%d")

    @property
    def id(self):
        return self._id

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description

    @property
    def date(self):
        return self._date

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, category='{self.category}')"