class Contributor:

    def __init__(self, i_d: int, name: str):
        self.id = i_d
        self.name = name

        self.total_cost = 0
        self.total_spent = 0
        self.balance = 0

        # self.to_receive = []
        # self.to_pay = []

    def update_total_cost(self, amount: float):
        self.total_cost += amount

    def update_total_expenditure(self, amount: float):
        self.total_spent += amount
