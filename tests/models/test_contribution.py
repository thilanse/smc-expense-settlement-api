from models.contribution import Contribution
from models.contributor import Contributor


def test_contribution():

    contributor = Contributor(1, "thilan")

    contribution = Contribution(1000, contributor)

    assert contribution.amount == 1000
    assert contribution.contributor.name == "thilan"
    assert contribution.contributor.id == 1
    assert contribution.contributor.total_cost == 0
    assert contribution.contributor.total_spent == 1000
