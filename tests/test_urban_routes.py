from data import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage
from helpers.utilities import retrieve_phone_code

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.driver.maximize_window()
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # 1. Configurar la dirección
    def test_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    # 2. Seleccionar la tarifa Comfort
    def test_select_comfort_tariff(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff_icon()
        assert self.routes_page.get_selected_tariff_text() == "Comfort"

    # 3. Rellenar el número de teléfono
    def test_add_phone_number(self):
        self.routes_page.add_phone_number(data.phone_number, retrieve_phone_code)
        # Verificación: el campo de teléfono ya no se muestra (modal cerrado)
        assert self.routes_page.get_test_add_phone_number() == data.phone_number

    # 4. Agregar una tarjeta de crédito
    def test_add_card(self):
        self.routes_page.add_card(data.card_number, data.card_code)

    # 5. Escribir un mensaje para el conductor
    def test_message_driver(self):
        self.routes_page.set_driver_message(data.message_for_driver)
        assert self.routes_page.get_driver_message() == data.message_for_driver

    # 6. Pedir una manta y pañuelos
    def test_blanket(self):
        self.routes_page.click_blanket()
        assert self.routes_page.is_blanket_selected() is True

    # 7. Pedir 2 helados
    def test_icecream(self):
        self.routes_page.add_icecream()
        self.routes_page.add_icecream()
        assert self.routes_page.get_icecream_value() == "2"

        assert self.routes_page.get_icecream_value() == "2"

    # 8. Aparece el modal para buscar un taxi
    def test_order_taxi(self):
        self.routes_page.click_order_taxi()
        assert self.routes_page.get_search_modal().is_displayed()

        assert self.routes_page.get_search_modal().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()