# Import from data.py and helpers.py

from selenium import webdriver

import data
import helpers
from data import ADDRESS_TO, ADDRESS_FROM, URBAN_ROUTES_URL, PHONE_NUMBER, MESSAGE_FOR_DRIVER
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod

    def setup_class(cls):

        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Test to see if server is still running
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def test_set_route(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        assert ADDRESS_TO and ADDRESS_FROM in urban_routes_page.get_addresses_entered()

    def test_select_supportive_plan(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.select_supportive_plan()
        urban_routes_page.get_supportive_class()
        assert urban_routes_page.get_supportive_class()

    def test_fill_phone_number(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.click_call_taxi()
        urban_routes_page.fill_phone_number()
        assert PHONE_NUMBER == urban_routes_page.get_phone_number()


    def test_fill_card(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.click_call_taxi()
        urban_routes_page.fill_card()
        assert urban_routes_page.get_card_accepted()

    def test_comment_for_driver(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.click_call_taxi()
        urban_routes_page.comment_for_driver()
        assert MESSAGE_FOR_DRIVER == urban_routes_page.get_driver_message()

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.select_supportive_plan()
        urban_routes_page.order_blanket_and_handkerchiefs()
        assert urban_routes_page.is_order_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.select_supportive_plan()
        urban_routes_page.order_2_ice_creams()
        assert urban_routes_page.get_ice_creams_ordered()

    def test_car_search_model_appears(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.select_supportive_plan()
        urban_routes_page.get_supportive_class()
        urban_routes_page.fill_phone_number()
        urban_routes_page.fill_card()
        urban_routes_page.comment_for_driver()
        urban_routes_page.order_taxi()
        assert urban_routes_page.get_order_complete()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()