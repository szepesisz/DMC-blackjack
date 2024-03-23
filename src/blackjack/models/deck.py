from typing import List
from itertools import product

from pydantic import (
    BaseModel
)

from blackjack.models.card import Card, SuitEnum, RankEnum


class Deck(BaseModel):
    deck_id: int
    cards: List[Card]

    def __init__(self, deck_id):
        _cards = []
        for s, r in product(SuitEnum, RankEnum):
            _cards.append(Card(suit=s, rank=r))
        super().__init__(
            cards=_cards,
            deck_id=deck_id
        )
