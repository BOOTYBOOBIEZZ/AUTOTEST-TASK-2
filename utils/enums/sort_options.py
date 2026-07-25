from enum import StrEnum


class SortOption(StrEnum):
    RELEVANCE = "relevance"
    PRICE_LOW_TO_HIGH = "price_asc"
    PRICE_HIGH_TO_LOW = "price_desc"
