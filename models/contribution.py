from models.contributor import Contributor


class Contribution:

    def __init__(self, amount: float, contributor: Contributor):
        self.amount = amount

        contributor.update_total_expenditure(amount)
        self.contributor = contributor

        