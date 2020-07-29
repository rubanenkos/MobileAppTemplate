from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdvancedPage(BasePage):

    ARROW = (By.ID, "com.google.android.calculator:id/arrow")
    SQRT = (By.ID, "com.google.android.calculator:id/op_sqrt")

    def tap_arrow(self):
        self.click(*self.ARROW)

    def open_advanced_operations_panel(self, coordinates=[(1030, 1228)]):
        self.tab_by_coordinates(coordinates)

    def tap_square_root(self):
        self.click(*self.SQRT)