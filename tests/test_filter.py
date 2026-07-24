from playwright.sync_api import Page
from pages.main_page import MainPage
from utils.config_reader import ConfigReader

config = ConfigReader()
base_url = config.get_nested("urls", "base_url")


def test_filter_low_to_high(page: Page, base_url: str):
    page.goto(base_url)
    main_page = MainPage(page)
    main_page.click_search_bar()
    search_query = "city"
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    main_page.wait_for_loader_dissappear()

    main_page.click_sort_select()

    main_page.sort_by_price_low_to_high()

    prices = main_page.get_prices(10)
    assert prices == sorted(prices)


def test_filter_high_to_low(page: Page, base_url: str):
    page.goto(base_url)
    main_page = MainPage(page)

    main_page.click_search_bar()
    search_query = "city"
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    main_page.wait_for_loader_dissappear()
    main_page.click_sort_select()

    main_page.sort_by_price_high_to_low()

    prices = main_page.get_prices(15)
    assert prices == sorted(prices)


def test_filter_low_to_high(page: Page, base_url: str):
    page.goto(base_url)
    main_page = MainPage(page)
    main_page.click_search_bar()
    search_query = "habits"
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    main_page.wait_for_loader_dissappear()

    main_page.click_sort_select()

    main_page.sort_by_price_low_to_high()

    prices = main_page.get_prices(10)
    assert prices == sorted(prices)


def test_filter_high_to_low(page: Page, base_url: str):
    page.goto(base_url)
    main_page = MainPage(page)
    main_page.click_search_bar()
    search_query = "habits"
    main_page.fill_search_bar(search_query)
    main_page.click_search_button()

    main_page.wait_for_loader_dissappear()

    main_page.click_sort_select()

    main_page.sort_by_price_high_to_low()

    prices = main_page.get_prices(15)
    assert prices == sorted(prices)