from fastapi import APIRouter

from models.contribution import Contribution
from models.contributor import Contributor
from models.event import Event
from models.expense import Expense
from routers.models.request_models import EventDTO

router = APIRouter()


@router.post("/transfer-settlement", tags=["Expense Controller"])
async def settle_transfers(event_request: EventDTO):

    # Convert EventRequest to Event object
    event = Event(event_request.name)

    for contributor_dto in event_request.contributors:
        contributor = Contributor(contributor_dto.id, contributor_dto.name)
        event.add_contributor(contributor)

    for expense_dto in event_request.expenses:
        expense = Expense(expense_dto.name)

        for contribution_dto in expense_dto.contributions:
            contributor = event.get_contributor(contribution_dto.contributor.id)
            contribution = Contribution(contribution_dto.amount, contributor)
            expense.add_contribution(contribution)

        event.add_expense(expense)

    transfers = event.calculate_transfers()

    return transfers



