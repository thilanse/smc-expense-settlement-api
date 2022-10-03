from src.models.contribution import Contribution
from src.models import Contributor
from src.models import Expense


def test_expense():

    contributor_1 = Contributor(1, "thilan")
    contributor_2 = Contributor(2, "bula")
    contributor_3 = Contributor(3, "chathu")

    contribution_1 = Contribution(1000, contributor_1)
    contribution_2 = Contribution(2000, contributor_2)
    contribution_3 = Contribution(0, contributor_3)

    expense = Expense("bowling")
    expense.add_contribution(contribution_1)
    expense.add_contribution(contribution_2)
    expense.add_contribution(contribution_3)

    assert expense.name == "bowling"
    assert len(expense.contributions) == 3
    assert expense.contributions[0] == contribution_1
    assert expense.contributions[1] == contribution_2
    assert expense.contributions[2] == contribution_3

    assert expense.get_total_cost() == 3000
    assert expense.get_average_cost() == 1000.0


