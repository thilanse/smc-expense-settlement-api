from src.models.contributor import Contributor
from src.models.event import Event
from src.models.expense import Expense
from src.services.expense_manager import ExpenseManager


def test_calculate_pending_transfers():
    event = Event("CCC Bowling + Dinner - Aug 26th")

    thilan = Contributor("thilan")
    omal = Contributor("omal")
    jitha = Contributor("jitha")
    chathu = Contributor("chathu")
    mindula = Contributor("mindula")

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
