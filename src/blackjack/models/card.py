from enum import Enum
from pydantic import (
    BaseModel
)


class SuitEnum(str, Enum):
    clubs = 'clubs'  # treff
    diamonds = 'diamonds'  # karo
    hearts = 'hearts'  # cour
    spades = 'spades'  # pikk


class RankEnum(str, Enum):
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    ten = '10'
    jack = 'J'
    queen = 'Q'
    king = 'K'
    ace = 'A'


class Card(BaseModel):
    suit: SuitEnum
    rank: RankEnum
