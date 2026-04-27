from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    # LOCALIZADORES
    # Direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Pedir taxi (botón principal)
    request_taxi_button = (By.XPATH, "//button[text()='Pedir un taxi']")

    # Tarifa Comfort
    comfort_tariff_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    comfort_tariff_assert = (By.XPATH,
                             "//div[contains(@class,'tcard') and .//div[text()='Comfort']]"
                             "//div[contains(@class,'tcard-title') and text()='Comfort']")
    # Validamos por título visible de la tarjeta seleccionada
    comfort_selected_card = (By.XPATH,
                             "//div[contains(@class,'tcard') and contains(@class,'active')]//div[text()='Comfort']")

    # Teléfono
    phone_number_button = (By.CSS_SELECTOR, 'div.np-button')  # Botón "Número de teléfono"
    phone_field = (By.ID, 'phone')
    next_phone_button = (By.XPATH, "//button[@type='submit' and contains(@class,'button') and text()='Siguiente']")
    phone_code_field = (By.ID, 'code')
    confirm_phone_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")

    # Método de pago / Tarjeta
    payment_method_button = (By.CSS_SELECTOR, 'div.pp-button.filled')  # Abre modal "Método de pago"
    add_card_button = (By.XPATH, "//div[@class='pp-row disabled']")  # "Agregar tarjeta"
    test_add_phone_number = (By.XPATH, "//div[@class= 'np-button filled']/div") # "Verificar el numero de telefono"
    test_add_card = (By.XPATH, "//div[@class='pp-value-text']") # "Verificar que diga tarjeta"
    card_number_field = (By.XPATH, "//div[@class='card-number-input']//input[@id='number']")
    card_code_field = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    link_card_button = (By.XPATH, "//div[contains(@class,'pp-buttons')]//button[text()='Agregar']")
    close_payment_modal_button = (By.CSS_SELECTOR, 'div.payment-picker.open button.close-button')

    # Mensaje al conductor
    message_driver_field = (By.ID, 'comment')

    # Manta y pañuelos (switch)
    blanket_switch = (By.XPATH,
                      "//div[@class='r-sw-label' and text()='Manta y pañuelos']/../div[@class='r-sw']//span[@class='slider round']")
    blanket_checkbox = (By.XPATH,
                        "//div[@class='r-sw-label' and text()='Manta y pañuelos']/../div[@class='r-sw']//input")

    # Helado
    icecream_plus = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/..//div[@class='counter-plus']")
    icecream_value = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/..//div[@class='counter-value']")

    # Pedir taxi (final) y modal de búsqueda
    order_taxi_button = (By.CSS_SELECTOR, 'button.smart-button')
    taxi_search_modal = (By.CSS_SELECTOR, 'div.order-body')
    car_search_title = (By.XPATH, "//div[contains(text(),'Buscar automóvil')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------- DIRECCIONES ----------
    def set_from(self, from_address):
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    # ---------- PEDIR TAXI ----------
    def click_request_taxi_button(self):
        self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)).click()

    # ---------- TARIFA COMFORT ----------
    def click_comfort_tariff_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff_icon)).click()

    def get_selected_tariff_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.comfort_selected_card)
        ).text

    # ---------- TELÉFONO ----------
    def click_phone_number_button(self):
        self.wait.until(EC.element_to_be_clickable(self.phone_number_button)).click()

    def set_phone_number(self, phone_number):
        self.wait.until(EC.visibility_of_element_located(self.phone_field)).send_keys(phone_number)

    def click_next_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.next_phone_button)).click()

    def set_phone_code(self, code):
        self.wait.until(EC.visibility_of_element_located(self.phone_code_field)).send_keys(code)

    def click_confirm_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_phone_button)).click()

    def add_phone_number(self, phone_number, retrieve_code_func):
        """Flujo completo de teléfono."""
        self.click_phone_number_button()
        self.set_phone_number(phone_number)
        self.click_next_phone()
        code = retrieve_code_func(self.driver)
        self.set_phone_code(code)
        self.click_confirm_phone()

    def get_test_add_phone_number(self):
        return self.driver.find_element(*self.test_add_phone_number).text

    # ---------- TARJETA ----------
    def click_payment_method(self):
        self.wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()

    def click_add_card(self):
        self.wait.until(EC.visibility_of_element_located(self.add_card_button)).click()

    def set_card_number(self, card_number):
        self.wait.until(EC.visibility_of_element_located(self.card_number_field)).send_keys(card_number)

    def set_card_code(self, card_code):
        code_input = self.wait.until(EC.visibility_of_element_located(self.card_code_field))
        code_input.send_keys(card_code)
        # TAB es necesario para habilitar el botón "Agregar"
        code_input.send_keys(Keys.TAB)

    def click_link_card(self):
        self.wait.until(EC.element_to_be_clickable(self.link_card_button)).click()

    def close_payment_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.close_payment_modal_button)).click()

    def add_card(self, card_number, card_code):
        """Flujo completo para agregar una tarjeta."""
        self.click_payment_method()
        self.click_add_card()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_link_card()
        self.close_payment_modal()

    def get_test_add_card(self):
        return self.driver.find_element(*self.test_add_card).text

    # ---------- MENSAJE AL CONDUCTOR ----------
    def set_driver_message(self, message):
        self.wait.until(EC.visibility_of_element_located(self.message_driver_field)).send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.message_driver_field).get_property('value')

    # ---------- MANTA Y PAÑUELOS ----------
    def click_blanket(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_switch)).click()

    def is_blanket_selected(self):
        return self.driver.find_element(*self.blanket_checkbox).is_selected()

    # ---------- HELADO ----------
    def add_icecream(self):
        self.wait.until(EC.element_to_be_clickable(self.icecream_plus)).click()

    def get_icecream_value(self):
        return self.wait.until(EC.visibility_of_element_located(self.icecream_value)).text

    # ---------- PEDIR TAXI FINAL ----------
    def click_order_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.order_taxi_button)).click()

    def get_search_modal(self):
        return self.wait.until(EC.visibility_of_element_located(self.taxi_search_modal))