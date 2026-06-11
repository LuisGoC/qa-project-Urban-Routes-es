from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi_button = (By.XPATH, '//button[@class="button round" and text()="Pedir un taxi"]')
    comfort_button = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))
        element.send_keys(from_address)

    def set_to(self, to_address):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.to_field))
        element.send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_order_a_taxi_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.order_a_taxi_button))
        element.click()

    def click_comfort_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.comfort_button))
        element.click()

    def get_comfort_rate(self):
        return self.driver.find_element(*self.comfort_button).text

