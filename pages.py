from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER
import time
import helpers
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    CALL_TAXI_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    #SUPPORTIVE_LOCATOR = (By.XPATH, '//img[@src="/static/media/kids.27f92282.svg"]')
    SUPPORTIVE_LOCATOR = (By.XPATH,  '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    SUPPORTIVE_ACTIVE_LOCATOR = (By.XPATH, '//div[@class="tcard active"]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@class="np-button"]')
    PHONE_NUMBER_MODAL = (By.XPATH, '//*[@id="phone"]')
    PHONE_NEXT_LOCATOR = (By.XPATH, '//button[normalize-space()="Next"]')
    CODE_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[normalize-space()="Confirm"]')
    PHONE_NUMBER_TEXT_LOCATOR = (By.XPATH, '//div[@class = "np-text"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    ADD_CARD_LOCATOR = (By.XPATH, '//img[@alt="plus"]')
    CARD_NUMBER_LOCATOR = (By.XPATH, '//input[@id="number"]')
    CARD_CODE_LOCATOR = (By.XPATH, '//input[@name="code"]')
    LINK_CARD_LOCATOR = (By. XPATH, '//button[normalize-space()="Link"]')
    CLOSE_PAYMENT_LOCATOR = (By. XPATH,'//div[@class="payment-picker open"]//div[@class="section active"]//button[@class="close-button section-close"]')
    DRIVER_MESSAGE_LOCATOR = (By. XPATH, '//div[@class="form"]//div//div[@class="input-container"]')
    BLANKET_HANDKERCHIEF_LOCATOR = (By. XPATH, '//div[text()= "Blanket and handkerchiefs"]//div[2]//span[@class = "slider round"]')
    ADD_ICE_CREAM_LOCATOR = (By.XPATH, '//div[text()="Ice cream"]')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//button[@class = "smart-button"]')

    #methods
    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        from_text = ADDRESS_FROM
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        to_text = ADDRESS_TO
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def click_call_taxi(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()
        time.sleep(2)
        supportive_locator = self.driver.find_element(*self.SUPPORTIVE_LOCATOR)
        active_class_name = "active"
        if active_class_name in supportive_locator.get_attribute("class"):
            pass
        else:
            supportive_locator.click()
            time.sleep(1)

    def get_supportive_class(self):
        active_element = self.driver.find_element(*self.SUPPORTIVE_LOCATOR)
        expected_class = "active"
        assert expected_class in active_element.get_attribute("class"), "Supportive is not selected."


    def fill_phone_number(self):
        phone_number = PHONE_NUMBER
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
        time.sleep(2)
        self.driver.find_element(*self.PHONE_NUMBER_MODAL).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_NEXT_LOCATOR).click()
        time.sleep(2)
        code = helpers.retrieve_phone_code(self.driver)
        time.sleep(1)
        self.driver.find_element(*self.CODE_LOCATOR).send_keys(code)
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_TEXT_LOCATOR).text

    def fill_card(self):
        card_number = CARD_NUMBER
        card_code = CARD_CODE
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)
        time.sleep(1)
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(card_code)
        time.sleep(1)
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element(*self.LINK_CARD_LOCATOR).click()
        time.sleep(1)
        self.driver.find_element(*self.CLOSE_PAYMENT_LOCATOR).click()
        time.sleep(1)
        card_accepted = self.driver.find_element(By.XPATH, '//div[contains(@class, "pp-value-text") and contains(text(), "Card")]')
        assert card_accepted

    def comment_for_driver(self):
        message = MESSAGE_FOR_DRIVER
        self.driver.find_element(*self.DRIVER_MESSAGE_LOCATOR).send_keys(message)

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR).click()

    def order_2_ice_creams(self):
        for i in range(2):
            self.driver.find_element(*self.ADD_ICE_CREAM_LOCATOR).click()

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()
