# Import from data.py and helpers.py

from selenium import webdriver

import data
import helpers
from data import ADDRESS_TO, ADDRESS_FROM, URBAN_ROUTES_URL, PHONE_NUMBER
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
        print("function created for set route")
        pass

    def test_select_supportive_plan(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_text = ADDRESS_FROM
        to_text = ADDRESS_TO
        urban_routes_page.enter_locations(from_text, to_text)
        urban_routes_page.select_supportive_plan()
        urban_routes_page.get_supportive_class()

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

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
            # Add in S8
        pass
        print("function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()