from src.models.contribution import Contribution
from src.models import Contributor
from src.models.event import Event
from src.models import Expense
from src.services import ExpenseManager


def test_calculate_pending_transfers():
    event = Event("CCC Bowling + Dinner - Aug 26th")

    thilan = Contributor(1, "thilan")
    omal = Contributor(2, "omal")
    jitha = Contributor(3, "jitha")
    chathu = Contributor(4, "chathu")
    mindula = Contributor(5, "mindula")

    event.add_contributor(thilan)
    event.add_contributor(omal)
    event.add_contributor(jitha)
    event.add_contributor(chathu)
    event.add_contributor(mindula)

    # Expenses
    drinks = Expense("Drinks")
    bowling = Expense("Bowling")
    basketball = Expense("Basketball")
    dinner = Expense("Playtrix dinner")

    # Expense Contributions
    drinks.add_contributor(thilan)
    drinks.add_contributor(omal)
    drinks.add_contributor(chathu)
    drinks.add_contributor(mindula)

    bowling.add_contributor(thilan)
    bowling.add_contributor(omal)
    bowling.add_contributor(jitha)
    bowling.add_contributor(chathu)
    bowling.add_contributor(mindula)

    basketball.add_contributor(thilan)
    basketball.add_contributor(omal)
    basketball.add_contributor(jitha)
    basketball.add_contributor(chathu)
    basketball.add_contributor(mindula)

    dinner.add_contributor(thilan)
    dinner.add_contributor(omal)
    dinner.add_contributor(jitha)
    dinner.add_contributor(chathu)
    dinner.add_contributor(mindula)

    drinks.add_contribution(thilan, 2800)
    bowling.add_contribution(thilan, 5000)
    basketball.add_contribution(omal, 2500)
    dinner.add_contribution(thilan, 13675)

    # Add expenses to event
    event.add_expense(drinks)
    event.add_expense(bowling)
    event.add_expense(basketball)
    event.add_expense(dinner)

    transfers = ExpenseManager.calculate_pending_transfers(event)

    assert transfers == [
        {'amount': 4935, 'from': 'chathu', 'to': 'thilan'},
        {'amount': 4935, 'from': 'mindula', 'to': 'thilan'},
        {'amount': 4235, 'from': 'jitha', 'to': 'thilan'},
        {'amount': 2435, 'from': 'omal', 'to': 'thilan'}
    ]


def test_calculate_expense_balances():
    contributor_1 = Contributor(1, "thilan")
    contributor_2 = Contributor(2, "bula")
    contributor_3 = Contributor(3, "chathu")

    contribution_1 = Contribution(1000, contributor_1)
    contribution_2 = Contribution(2000, contributor_2)
    contribution_3 = Contribution(0, contributor_3)
    expense_1 = Expense("bowling")
    expense_1.add_contribution(contribution_1)
    expense_1.add_contribution(contribution_2)
    expense_1.add_contribution(contribution_3)

    contribution_4 = Contribution(1000, contributor_1)
    contribution_5 = Contribution(1000, contributor_2)
    expense_2 = Expense("food")
    expense_2.add_contribution(contribution_4)
    expense_2.add_contribution(contribution_5)

    event = Event("outing")
    event.add_contributor(contributor_1)
    event.add_contributor(contributor_2)
    event.add_contributor(contributor_3)
    event.add_expense(expense_1)
    event.add_expense(expense_2)
    event.update_contributor_totals()

    to_receive, to_pay = ExpenseManager.calculate_expense_balances(event)

    assert to_receive == {'bula': 1000}
    assert to_pay == {'chathu': 1000, 'thilan': 0}


def test_event_obj():

    event = {
        "name": "event 1",
        "contributors": [
            {"id": 1, "name": "thilan"},
            {"id": 2, "name": "chathu"},
            {"id": 3, "name": "bula"},
        ],
        "expenses": [
            {
                "id": 1,
                "name": "bowling",
                "participants": [1, 2],
                "contributions": [
                    {"amount": 1000, "contributor": 1}
                ]
            }
        ]

    }
