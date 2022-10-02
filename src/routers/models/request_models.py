from typing import List

from pydantic import BaseModel


class ContributorDTO(BaseModel):
    id: int
    name: str


class ContributionDTO(BaseModel):
    amount: float
    contributor: ContributorDTO


class ExpenseDTO(BaseModel):
    id: int
    name: str
    contributions: List[ContributionDTO]


class EventDTO(BaseModel):
    name: str
    contributors: List[ContributorDTO]
    expenses: List[ExpenseDTO]



