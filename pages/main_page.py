from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_bar = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def click_search_bar(self):
        self.search_bar.click()

    def fill_search_bar(self, name):
        self.search_bar.fill(name)

    def click_search_button(self):
        self.search_button.click()
