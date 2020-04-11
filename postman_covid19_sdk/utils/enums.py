from enum import Enum

__all__ = [
    "CategoryType",
    "StatusType"
]


class CategoryType(Enum):
    DEFAULT = None
    LIVE = 'live'
    TOTAL = 'total'


class StatusType(Enum):
    CONFIRMED = "confirmed"
    RECOVERED = "recovered"
    DEATHS = "deaths"
