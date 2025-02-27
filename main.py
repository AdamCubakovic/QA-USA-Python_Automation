# Import from data.py and helpers.py

import data
import helpers
from data import URBAN_ROUTES_URL
from helpers import is_url_reachable

class TestUrbanRoutes:
    @classmethod
    # Test to see if server is still running
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
        # Since is_url_reachable is boolean, this is asking if that function is True.
        # Simpler way of writing if function == True:

            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def test_set_route(self):
        #Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

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
        for i in range(0,1):
            # Add in S8
            pass
        print("function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model")
        pass