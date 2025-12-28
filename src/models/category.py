class Category:
    def __init__(self):
        self.categories = [
            "Food", "Transport", "Utilities",
            "Entertainment", "Other"
        ]

    def add_category(self, new_category):
        if new_category not in self.categories:
            self.categories.append(new_category)

    def view_category(self):
        return self.categories