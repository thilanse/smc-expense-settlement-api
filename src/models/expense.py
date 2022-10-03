from typing import List

from src.models.contribution import Contribution


class Expense:

    def __init__(self, name: str):
        self.name = name
        self.contributions: List[Contribution] = []

    def add_contribution(self, contribution: Contribution):
        self.contributions.append(contribution)

    def get_total_cost(self):
        total_cost = sum(c.amount for c in self.contributions)
        return total_cost

    def get_average_cost(self):
        return self.get_total_cost() / len(self.contributions)
