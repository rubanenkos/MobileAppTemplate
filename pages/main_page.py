from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    MAIN_SCREEN = (By.ID, "com.google.android.calculator:id/main_calculator")
    FORMULA_SCREEN = (By.ID, "com.google.android.calculator:id/formula")
    RESULT = (By.ID, "com.google.android.calculator:id/result_final")
    POINT = (By.ID, "com.google.android.calculator:id/dec_point")
    CLEAR = (By.ID, "com.google.android.calculator:id/clr")
    DELETE = (By.ID, "com.google.android.calculator:id/del")
    DIGIT = "com.google.android.calculator:id/digit_"

    EQUALITY = (By.ID, "com.google.android.calculator:id/eq")
    PLUS = (By.ID, "com.google.android.calculator:id/op_add")
    MINUS = (By.ID, "com.google.android.calculator:id/op_sub")
    MULTIPLY = (By.ID, "com.google.android.calculator:id/op_mul")
    DIVIDE = (By.ID, "com.google.android.calculator:id/op_div")

    def verify_main_screen(self):
        return self.find_element(*self.MAIN_SCREEN)

    def tap_digit(self, given_figure):
        digit = (By.ID, self.DIGIT + given_figure)
        self.click(*digit)

    def tap_delete(self):
        self.click(*self.DELETE)

    def tap_point(self):
        self.click(*self.POINT)

    def tap_clear(self):
        self.click(*self.CLEAR)

    def tap_equality(self):
        self.click(*self.EQUALITY)

    def tap_plus(self):
        self.click(*self.PLUS)

    def tap_minus(self):
        self.click(*self.MINUS)

    def tap_divide(self):
        self.click(*self.DIVIDE)

    def tap_multiply(self):
        self.click(*self.MULTIPLY)

    def get_result(self):
        return self.find_element(*self.RESULT).text

    def get_screen_status(self):
        return self.find_element(*self.FORMULA_SCREEN).text

