from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi_button = (By.XPATH, '//button[@class="button round" and text()="Pedir un taxi"]')
    comfort_button = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_number_button = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.ID, 'phone')
    phone_number_next_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    phone_number_code_field = (By.ID, 'code')
    phone_number_confirm_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    payment_method_button = (By.CLASS_NAME, 'pp-value-text')
    add_card_button = (By.XPATH, '(//div[@class="pp-title"])[2]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, '(//input[@id="code"])[2]')
    card_title = (By.XPATH, '//div[@class="head" and text()="Agregar tarjeta"]')
    submit_card_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    payment_method_close_button = (By.XPATH, '(//button[@class="close-button section-close"])[3]')

    def __init__(self, driver):
        self.driver = driver

    def set_from_field(self, from_address):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))
        element.send_keys(from_address)

    def set_to_field(self, to_address):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.to_field))
        element.send_keys(to_address)

    def get_from_field(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to_field(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from_field(address_from)
        self.set_to_field(address_to)

    def click_order_a_taxi_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.order_a_taxi_button))
        element.click()

    def click_comfort_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.comfort_button))
        element.click()

    def get_comfort_rate(self):
        return self.driver.find_element(*self.comfort_button).text

    def click_phone_number_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.phone_number_button))
        element.click()

    def set_phone_number_field(self, phone_number):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_number_field))
        element.send_keys(phone_number)

    def click_phone_number_next_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.phone_number_next_button))
        element.click()

    def set_phone_number_code_field(self, code):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_number_code_field))
        element.send_keys(code)

    def click_phone_number_confirm_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.phone_number_confirm_button))
        element.click()

    def set_phone_number(self, phone_number):
        self.click_phone_number_button()
        self.set_phone_number_field(phone_number)
        self.click_phone_number_next_button()
        self.set_phone_number_code_field(retrieve_phone_code(self.driver))
        self.click_phone_number_confirm_button()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).text

    def click_payment_method_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.payment_method_button))
        element.click()

    def get_payment_method(self):
        return self.driver.find_element(*self.payment_method_button).text

    def click_add_card_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.add_card_button))
        element.click()

    def set_card_number_field(self, number):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.card_number_field))
        element.send_keys(number)

    def set_card_code_field(self, code):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.card_code_field))
        element.send_keys(code)

    def click_card_title(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.card_title))
        element.click()

    def click_submit_card_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.submit_card_button))
        element.click()

    def click_payment_method_close_button(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.payment_method_close_button))
        element.click()

    def set_payment_method(self, card_number, card_code):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.set_card_number_field(card_number)
        self.set_card_code_field(card_code)
        self.click_card_title()
        self.click_submit_card_button()
        self.click_payment_method_close_button()


