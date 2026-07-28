from enum import StrEnum

from playwright.sync_api import Page


class SortOption(StrEnum):
    PRICE_LOW_TO_HIGH = "price_asc"
    PRICE_HIGH_TO_LOW = "price_desc"


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_select = page.get_by_test_id("filter-sort")
        self.search_bar = page.get_by_test_id("search-input")
        self.loader = page.get_by_test_id("results-loader-svg")
        self.apply_button = page.get_by_test_id("apply-filters-button")
        self.search_button = page.get_by_test_id("search-button")

    def click_search_bar(self):
        self.search_bar.click()

    def fill_search_bar(self, name):
        self.search_bar.fill(name)

    def click_search_button(self):
        self.search_button.click()

    def wait_for_loader_dissappear(self):
        self.loader.wait_for(state="visible")
        self.loader.wait_for(state="hidden")

    def click_sort_select(self):
        self.sort_select.click()

    def sort_by_price_low_to_high(self):
        self.sort_select.select_option(SortOption.PRICE_LOW_TO_HIGH)

    def sort_by_price_high_to_low(self):
        self.sort_select.select_option(SortOption.PRICE_HIGH_TO_LOW)

    def apply_filter(self):
        self.apply_button.click()

    def get_prices(self, n):
        prices = []
        for i in range(1, n + 1):
            price_locator = self.page.locator(
                f'[data-testid="search-result-price-{i}"]'
            )
            price_text = price_locator.text_content()
            prices.append(price_text)
        return prices
