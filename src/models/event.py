from src.models.contributor import Contributor
from src.models.expense import Expense


class Event:

    def __init__(self, name: str):
        self.name = name
        self.expenses = []
        self.contributors = []

    @property
    def total_cost(self):
        expense_costs = [e.total_cost for e in self.expenses]
        return sum(expense_costs)

    def add_contributor(self, contributor: Contributor):
        self.contributors.append(contributor.name)

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    @property
    def cost_per_person(self):
        cost_per_person = dict.fromkeys(self.contributors, 0)
        for e in self.expenses:
            per_person = e.cost_per_person
            for person in e.contributions:
                cost_per_person[person] += per_person
        return cost_per_person

    @property
    def total_spent_per_person(self):
        cost_per_person = dict.fromkeys(self.contributors, 0)
        for e in self.expenses:
            for contributor, amount in e.contributions.items():
                cost_per_person[contributor] += amount
        return cost_per_person
