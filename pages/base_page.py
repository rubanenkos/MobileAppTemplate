class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        element = self.driver.find_element(*locator)
        element.click()

    def tab_by_coordinates(self, list_of_coordinates):
        self.driver.tap(list_of_coordinates)
