from src.models.contributor import Contributor


def test_contributor():

    contributor = Contributor(1, "thilan")

    assert contributor.id == 1
    assert contributor.name == "thilan"

    assert contributor.total_cost == 0
    assert contributor.total_spent == 0

    contributor.update_total_cost(500)
    contributor.update_total_cost(100)
    contributor.update_total_expenditure(1000)
    contributor.update_total_expenditure(200)

    assert contributor.total_cost == 600
    assert contributor.total_spent == 1200
