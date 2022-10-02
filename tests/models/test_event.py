from src.models.contribution import Contribution
from src.models.contributor import Contributor
from src.models.event import Event
from src.models.expense import Expense


def mock_event_1():

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

    return event


def mock_event_2():
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
    drinks.add_contribution(Contribution(2800, thilan))
    drinks.add_contribution(Contribution(0, omal))
    drinks.add_contribution(Contribution(0, chathu))
    drinks.add_contribution(Contribution(0, mindula))

    bowling = Expense("Bowling")
    bowling.add_contribution(Contribution(5000, thilan))
    bowling.add_contribution(Contribution(0, omal))
    bowling.add_contribution(Contribution(0, jitha))
    bowling.add_contribution(Contribution(0, chathu))
    bowling.add_contribution(Contribution(0, mindula))

    basketball = Expense("Basketball")
    basketball.add_contribution(Contribution(0, thilan))
    basketball.add_contribution(Contribution(2500, omal))
    basketball.add_contribution(Contribution(0, jitha))
    basketball.add_contribution(Contribution(0, chathu))
    basketball.add_contribution(Contribution(0, mindula))

    dinner = Expense("Playtrix dinner")
    dinner.add_contribution(Contribution(13675, thilan))
    dinner.add_contribution(Contribution(0, omal))
    dinner.add_contribution(Contribution(0, jitha))
    dinner.add_contribution(Contribution(0, chathu))
    dinner.add_contribution(Contribution(0, mindula))

    # Add expenses to event
    event.add_expense(drinks)
    event.add_expense(bowling)
    event.add_expense(basketball)
    event.add_expense(dinner)

    return event

def mock_event_3():
    event = Event("King of the Mambo - Aug 5th")

    bula = Contributor(1, "bula")
    thilan = Contributor(2, "thilan")
    omal = Contributor(3, "omal")
    jitha = Contributor(4, "jitha")
    chamara = Contributor(5, "chamara")
    sanduni = Contributor(6, "sanduni")
    chathu = Contributor(7, "chathu")
    shaki = Contributor(8, "shaki")

    event.add_contributor(bula)
    event.add_contributor(thilan)
    event.add_contributor(omal)
    event.add_contributor(jitha)
    event.add_contributor(chamara)
    event.add_contributor(sanduni)
    event.add_contributor(chathu)
    event.add_contributor(shaki)

    # Expenses
    pillawoos = Expense("Pillawoos")
    pillawoos.add_contribution(Contribution(0, bula))
    pillawoos.add_contribution(Contribution(0, thilan))
    pillawoos.add_contribution(Contribution(8060, omal))
    pillawoos.add_contribution(Contribution(0, jitha))
    pillawoos.add_contribution(Contribution(0, chamara))
    pillawoos.add_contribution(Contribution(0, sanduni))
    pillawoos.add_contribution(Contribution(0, chathu))
    pillawoos.add_contribution(Contribution(0, shaki))

    mambo = Expense("Mambo dinner")
    mambo.add_contribution(Contribution(28991.50, bula))
    mambo.add_contribution(Contribution(0, thilan))
    mambo.add_contribution(Contribution(0, omal))
    mambo.add_contribution(Contribution(0, jitha))
    mambo.add_contribution(Contribution(0, chamara))
    mambo.add_contribution(Contribution(0, sanduni))
    mambo.add_contribution(Contribution(0, chathu))
    mambo.add_contribution(Contribution(0, shaki))


    # Add expenses to event
    event.add_expense(pillawoos)
    event.add_expense(mambo)

    return event


def test_event():

    event = mock_event_1()
    event.update_contributor_totals()

    assert event.name == "outing"
    assert len(event.contributors) == 3
    assert len(event.expenses) == 2

    assert event.contributors[0].id == 1
    assert event.contributors[0].name == "thilan"
    assert event.contributors[0].total_cost == 2000
    assert event.contributors[0].total_spent == 2000

    assert event.contributors[1].id == 2
    assert event.contributors[1].name == "bula"
    assert event.contributors[1].total_cost == 2000
    assert event.contributors[1].total_spent == 3000

    assert event.contributors[2].id == 3
    assert event.contributors[2].name == "chathu"
    assert event.contributors[2].total_cost == 1000
    assert event.contributors[2].total_spent == 0


def test_calculate_transfers_event_1():

    event = mock_event_1()

    transfers = event.calculate_transfers()

    assert len(transfers) == 1

    assert transfers[0].amount == 1000
    assert transfers[0].to_pay.name == "chathu"
    assert transfers[0].to_receive.name == "bula"


def test_calculate_transfers_event_2():

    event = mock_event_2()

    transfers = event.calculate_transfers()

    assert len(transfers) == 4

    assert transfers[0].amount == 4935
    assert transfers[0].to_pay.name == "mindula"
    assert transfers[0].to_receive.name == "thilan"

    assert transfers[1].amount == 4935
    assert transfers[1].to_pay.name == "chathu"
    assert transfers[1].to_receive.name == "thilan"

    assert transfers[2].amount == 4235
    assert transfers[2].to_pay.name == "jitha"
    assert transfers[2].to_receive.name == "thilan"

    assert transfers[3].amount == 2435
    assert transfers[3].to_pay.name == "omal"
    assert transfers[3].to_receive.name == "thilan"


def test_calculate_transfers_event_3():

    event = mock_event_3()

    transfers = event.calculate_transfers()

    assert len(transfers) == 7

    assert transfers[0].amount == 4631
    assert transfers[0].to_pay.name == "shaki"
    assert transfers[0].to_receive.name == "bula"

    assert transfers[1].amount == 4631
    assert transfers[1].to_pay.name == "chathu"
    assert transfers[1].to_receive.name == "bula"

    assert transfers[2].amount == 4631
    assert transfers[2].to_pay.name == "sanduni"
    assert transfers[2].to_receive.name == "bula"

    assert transfers[3].amount == 4631
    assert transfers[3].to_pay.name == "chamara"
    assert transfers[3].to_receive.name == "bula"

    assert transfers[4].amount == 4631
    assert transfers[4].to_pay.name == "jitha"
    assert transfers[4].to_receive.name == "bula"

    assert transfers[5].amount == 4631
    assert transfers[5].to_pay.name == "thilan"
    assert transfers[5].to_receive.name == "omal"

    assert transfers[6].amount == 1202
    assert transfers[6].to_pay.name == "omal"
    assert transfers[6].to_receive.name == "bula"


