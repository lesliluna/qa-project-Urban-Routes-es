from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:

    #LOCALIZADORES
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    request_taxi_button = (By.CSS_SELECTOR, '.button.round')

    comfort_tariff_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_tariff_assert =(By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')

    phone_number_button = (By.CSS_SELECTOR, 'number-picker')
    next_phone_button = (By.XPATH, "//button[@type='submit'][@class='button full']")
    phone_option = (By.XPATH, '//div[text()="Número de teléfono"]')
    phone_field = (By.ID, 'phone')
    phone_code = (By.ID, 'code')
    confirm_phone_button = (By.XPATH, '//button[text()="Confirmar"]')

    add_card_button = (By.XPATH, '//div[text()="Método de pago" and @class= "pp-text"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.ID, 'code')
    link_card_button = (By.XPATH, '//button[text()="Agregar"]')
    close_button = (By.CSS_SELECTOR, 'close-button section-close')

    message_driver_field = (By.ID, 'comment')

    blanket_switch = (By.XPATH, '//span[text()="Manta y pañuelos"]/..//input')

    icecream_plus = (By.XPATH, '//span[text()="Helado"]/..//button[@class="counter-plus"]')
    icecream_value = (By.XPATH, '//span[text()="Helado"]/..//div[@class="counter-value"]')

    order_taxi_button = (By.XPATH, '//button[text()="Pedir taxi"]')

    taxi_search_modal = (By.XPATH, '//div[contains(text(),"Buscar automóvil")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    #DIRECCIONES
    def set_from(self, from_address):
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):     #Paso 2 Obtener el elemento
        self.set_from(address_from)
        self.set_to(address_to)

    #PEDIR_TAXI
    def get_request_taxi_button(self):
        return self.wait.until (
        EC.element_to_be_clickable (self.request_taxi_button))

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    #TARIFA_COMFORT
    def get_comfort_tariff_icon(self):
        return self.wait.until (
            EC.element_to_be_clickable (self.comfort_tariff_icon))

    def click_comfort_tariff_icon(self):
        self.get_comfort_tariff_icon().click()

    def get_comfort_tariff_assert(self):
        return self.wait.until (
            EC.visibility_of_element_located (self.comfort_tariff_assert))

    def read_comfort_tariff_assert(self):
        return self.get_comfort_tariff_assert().text

    #TELEFONO
    def click_phone_number(self):
        self.wait.until(EC.visibility_of_element_located(self.phone_option)) .click()
    def set_phone_number(self, phone_number):
        WebDriverWait (self.driver, 5).until(EC.visibility_of_element_located(self.phone_field))
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def click_next_phone(self):
        self.driver.find_element(*self.next_phone_button).click()

    def set_phone_code(self, code):
        self.wait.until(
            EC.visibility_of_element_located(self.phone_code)
        ).send_keys(code)

    def confirm_phone(self):
        self.driver.find_element(*self.confirm_phone_button).click()

    #TARJETA
    def click_add_card(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()

    def set_card_number(self, card_number):
        self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def set_card_code(self, card_code):
        code_input = self.wait.until(
            EC.visibility_of_element_located(self.card_code_field))
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

    def click_link_card(self):
        self.wait.until(
            EC.element_to_be_clickable(self.link_card_button)
        ).click()

    #MENSAJE
    def set_driver_message(self, message):
        self.wait.until(
            EC.visibility_of_element_located(self.message_driver_field)
        ).send_keys(message)

    #MANTA_Y_PAÑUELOS
    def click_blanket(self):
        self.wait.until(
            EC.element_to_be_clickable(self.blanket_switch)
        ).click()

    #HELADO
    def add_icecream(self):
        self.wait.until(
            EC.element_to_be_clickable(self.icecream_plus)
        ).click()

    def get_icecream_value(self):
        return self.driver.find_element(*self.icecream_value).text

    #PEDIR_TAXI_FINAL
    def click_order_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(self.order_taxi_button)
        ).click()

    def get_search_modal(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.taxi_search_modal)
        )