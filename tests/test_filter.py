from itertools import product

import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage
from pages.search_page import SearchPage, SortOption
from utils.config_reader import ConfigReader

config = ConfigReader()
# base_url = config.get_nested("urls", "base_url")
# search_url = config.get_nested("urls", "search_url")

SORTS = [(SortOption.PRICE_LOW_TO_HIGH), (SortOption.PRICE_HIGH_TO_LOW)]
QUERIES = ["city", "habits"]
NUMS = [10, 15]

COMBINATIONS = list(product(SORTS, QUERIES, NUMS))


@pytest.mark.parametrize("sort_type, search_query, n", COMBINATIONS)
def test_filter(
    page: Page,
    sort_type: SortOption,
    base_url: str,
    search_query: str,
    n: int,
):
    page.goto(base_url)
    main_page = MainPage(page)
    main_page.click_search_bar()
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    search_page = SearchPage(page)

    search_page.click_sort_select()
    search_page.sort_by(sort_type)
    search_page.wait_for_loader_dissappear()

    prices = search_page.get_prices(n)

    if sort_type == SortOption.PRICE_LOW_TO_HIGH:
        actual = prices
        expected = sorted(prices)
        assert actual == expected, (
            f"Prices not sorted ascending.\nExpected: {expected}\nActual: {actual}"
        )
    else:
        actual = prices
        expected = sorted(prices, reverse=True)
        assert actual == expected, (
            f"Prices not sorted descending.\nExpected: {expected}\nActual: {actual}"
        )
