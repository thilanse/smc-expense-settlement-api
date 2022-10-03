from src.models.contributor import Contributor


class Transfer:

    def __init__(self, debtor: Contributor, creditor: Contributor, amount: float):
        self.to_pay = debtor
        self.to_receive = creditor
        self.amount = amount
