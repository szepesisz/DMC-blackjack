from fastapi import (
    APIRouter
)

from blackjack.models import Deck

router = APIRouter()


@router.get(
    path='/deck',
    response_model=Deck
)
def get_deck():
    return Deck(deck_id=1)
