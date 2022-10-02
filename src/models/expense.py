from src.models.contributor import Contributor


class Expense:

    def __init__(self, name: str):
        self.name = name
        self.contributions = {}

    @property
    def total_cost(self):
        return sum(self.contributions.values())

    @property
    def cost_per_person(self):
        if not self.contributions:
            return 0
        return self.total_cost / len(self.contributions)

    def add_contribution(self, contributor: Contributor, amount: float):
        if contributor.name not in self.contributions:
            raise KeyError(f"Contributor '{contributor.name}' not added to Expense.")
        self.contributions[contributor.name] = amount

    def add_contributor(self, contributor: Contributor):
        if contributor.name not in self.contributions:
            self.contributions[contributor.name] = 0
