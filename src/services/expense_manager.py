from src.models.event import Event


class ExpenseManager:

    @staticmethod
    def calculate_expense_balances(event: Event):
        to_receive = {}
        to_pay = {}
        for person in event.contributors:
            total_spent = event.total_spent_per_person[person]
            actual_cost = event.cost_per_person[person]
            amount_to_transfer = total_spent - actual_cost
            if amount_to_transfer > 0:
                to_receive[person] = abs(int(amount_to_transfer))
            else:
                to_pay[person] = abs(int(amount_to_transfer))

        to_receive = dict(sorted(to_receive.items(), key=lambda x: x[1], reverse=True))
        to_pay = dict(sorted(to_pay.items(), key=lambda x: x[1], reverse=True))

        return to_receive, to_pay

    @staticmethod
    def calculate_pending_transfers(event: Event):

        to_receive, to_pay = ExpenseManager.calculate_expense_balances(event)

        transfers = []
        carry_forward_pay = None
        carry_forward = 0
        for person_to_receive in to_receive:
            if carry_forward > 0:
                transfers.append({
                    "from": person_to_receive,
                    "to": carry_forward_pay,
                    "amount": carry_forward
                })
            remaining = to_receive[person_to_receive] + carry_forward

            to_remove = []
            for person_to_pay, amount in to_pay.items():
                if (remaining - amount) >= 0:
                    remaining -= amount
                    transfers.append({
                        "from": person_to_pay,
                        "to": person_to_receive,
                        "amount": amount
                    })
                    to_remove.append(person_to_pay)
                else:
                    break

            for x in to_remove:
                to_pay.pop(x)
            carry_forward = remaining
            carry_forward_pay = person_to_receive

        return transfers
    