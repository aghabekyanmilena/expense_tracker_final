# class Expense:
	# def __init__(self, amount, category, description, date=None):
	# 	self._amount = amount
	# 	self._category = category
	# 	self._description = description
	# 	self._date = date if date else datetime.now().strftime("%Y-%m-%d")

	# @property
	# def amount(self):
	# 	return self._amount

	# @amount.setter
	# def amount(self, value):
	# 	if value < 0:
	# 		raise ValueError("Amount cannot be negative.")
	# 	self._amount = value

	# @property
	# def category(self):
	# 	return self._category

	# @property
	# def description(self):
	# 	return self._description

	# @property
	# def date(self):
	# 	return self._date

	# def __str__(self):
	# 	return f"{self.date} | {self.category} | {self.amount} | {self.description}"

	# def __repr__(self):
	# 	return f"Expense(amount={self.amount}, category='{self.category}')"


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

    def __eq__(self, other):
        return isinstance(other, Expense) and self.id == other.id
