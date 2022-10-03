from typing import List

from src.models.contributor import Contributor
from src.models.expense import Expense
from src.models.transfer import Transfer


class Event:

    def __init__(self, name: str):
        self.name = name
        self.expenses: List[Expense] = []
        self.contributors: List[Contributor] = []

    def get_contributor(self, contributor_id: int):
        contributor = next(c for c in self.contributors if c.id == contributor_id)
        return contributor

    def add_contributor(self, contributor: Contributor):
        self.contributors.append(contributor)

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def get_total_cost(self):
        expense_costs = [e.get_total_cost() for e in self.expenses]
        return sum(expense_costs)

    def update_contributor_totals(self):

        # Update total cost for each contributor
        for expense in self.expenses:
            expense_average_cost = expense.get_average_cost()
            for contribution in expense.contributions:
                contribution.contributor.update_total_cost(expense_average_cost)

        # Update to_receive and to_pay for each contributor
        for contributor in self.contributors:
            contributor.balance = contributor.total_cost - contributor.total_spent

    def settle_contributor_balances(self, transfers: List[Transfer], ignore_overpayments=True) -> List[Transfer]:

        for creditor in self.contributors:

            for debtor in reversed(self.contributors):
                if creditor.balance >= 0 or debtor.balance <= 0:
                    continue

                if ignore_overpayments and abs(creditor.balance) < debtor.balance:
                    continue

                # TODO: replace print statements with log debug statements
                print(f"{creditor.name}:{creditor.balance}, {debtor.name}:{debtor.balance}")

                # settle balance
                settlement_amount = debtor.balance
                creditor.balance += debtor.balance
                debtor.balance = 0

                print(f"{creditor.name}:{creditor.balance}, {debtor.name}:{debtor.balance}")
                print()

                transfer = Transfer(debtor, creditor, abs(int(settlement_amount)))
                transfers.append(transfer)

        return transfers

    def calculate_transfers(self) -> List[Transfer]:

        self.update_contributor_totals()

        # Sort based on balances and create transfers by ignoring overpayments
        # overpayments mean, if the debtor has a larger amount to balance than the creditor,
        # then, if the debtor were to proceed with the transfer, he/she would be overpaying the creditor.
        # Hence, the creditor will then have a positive balance.
        # Ignore the transfer, if there is an overpayment
        self.contributors.sort(key=lambda x: x.balance)
        transfers = self.settle_contributor_balances([], ignore_overpayments=True)

        # Sort based on balances again, and this time settle the transfers by allowing overpayments.
        # The whole purpose of this sorting and settling twice is so that each contributor will only need
        # to perform a transfer once. This will improve the user experience and hassle for the contributors
        # when performing the transfers.
        self.contributors.sort(key=lambda x: x.balance)
        transfers = self.settle_contributor_balances(transfers, ignore_overpayments=False)

        return transfers

