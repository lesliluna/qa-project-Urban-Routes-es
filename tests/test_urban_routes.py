from data import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff_icon()
        assert self.routes_page.read_comfort_tariff_assert() == "Manta y pañuelos"

    def test_add_phone_number(self):
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_next_phone()

        code = retrieve_phone_code(self.driver)

        self.routes_page.set_phone_code(code)
        self.routes_page.confirm_phone()

    def test_add_card(self):
        self.routes_page.click_add_card()

        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)

        self.routes_page.click_link_card()

    def test_message_driver(self):
        self.routes_page.set_driver_message(data.message_for_driver)

    def test_blanket(self):
        self.routes_page.click_blanket()

    def test_icecream(self):
        self.routes_page.add_icecream()
        self.routes_page.add_icecream()

        assert self.routes_page.get_icecream_value() == "2"

    def test_order_taxi(self):
        self.routes_page.click_order_taxi()

        assert self.routes_page.get_search_modal().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
