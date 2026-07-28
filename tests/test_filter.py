import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage
from pages.search_page import SearchPage
from utils.config_reader import ConfigReader

config = ConfigReader()
base_url = config.get_nested("urls", "base_url")
search_url = config.get_nested("urls", "search_url")


@pytest.mark.parametrize("search_query, n", [("city", 10), ("habits", 10)])
def test_filter_low_to_high(page: Page, search_query, n):
    page.goto(base_url)
    main_page = MainPage(page)
    main_page.click_search_bar()
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    page.goto(search_url)
    search_page = SearchPage(page)

    search_page.click_sort_select()
    search_page.sort_by_price_low_to_high()
    search_page.wait_for_loader_dissappear()

    prices = search_page.get_prices(n)

    actual = prices
    expected = sorted(prices)
    assert actual == expected, (
        f"Prices not sorted descending.\nExpected: {expected}\nActual: {actual}"
    )


@pytest.mark.parametrize("search_query, n", [("city", 15), ("habits", 15)])
def test_filter_high_to_low(page: Page, search_query, n):
    page.goto(base_url)
    main_page = MainPage(page)
    main_page.click_search_bar()
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    page.goto(search_url)
    search_page = SearchPage(page)

    search_page.click_sort_select()
    search_page.sort_by_price_high_to_low()
    search_page.wait_for_loader_dissappear()

    prices = search_page.get_prices(n)

    actual = prices
    expected = sorted(prices, reverse=True)
    assert actual == expected, (
        f"Prices not sorted descending.\nExpected: {expected}\nActual: {actual}"
    )
