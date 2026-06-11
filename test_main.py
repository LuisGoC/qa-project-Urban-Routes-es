import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from_field() == address_from
        assert routes_page.get_to_field() == address_to

    def test_set_comfort_rate(self):
        rate = data.rate
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_a_taxi_button()
        routes_page.click_comfort_button()
        assert routes_page.get_comfort_rate() == rate

    def test_set_phone_number(self):
        phone = data.phone_number
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_phone_number() == "Número de teléfono"
        routes_page.set_phone_number(phone)
        assert routes_page.get_phone_number() == phone


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
