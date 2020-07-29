from pages.advanced_page import AdvancedPage
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.advanced_page = AdvancedPage(driver)
