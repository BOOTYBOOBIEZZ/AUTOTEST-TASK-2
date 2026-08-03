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
        self.article_card = page.locator("article.news-card")

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

    def sort_by(self, option: SortOption):
        self.sort_select.select_option(option)

    def apply_filter(self):
        self.apply_button.click()

    def get_prices(self, n: int) -> list[int]:
        cards = self.article_card.all()[:n]

        prices = []
        for card in cards:
            price_attr = card.locator("[data-price]").get_attribute("data-price")
            if price_attr is None:
                raise ValueError("data-price attribute not found in card")
            prices.append(int(price_attr))

        return prices
