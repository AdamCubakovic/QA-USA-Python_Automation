Test Overview

This script tested the ordering of a taxi in the Urban Routes app. The goal was to test the ordering of a "Supportive" type of taxi. This included entering the To and From address, selecting the taxi type, filling in the user's phone number, adding a credit card, writing a comment for the taxi driver, selecting optional blankets and handkerchiefs, selecting two ice creams, and placing the order for the taxi.

This was done by:
1. Adding setup and teardown class as a classmethod to main.py.
2. Using POM to declare a class for the Urban Routes main page in pages.py and adding all necessary Selenium imports.
3. Adding XPATH and By.ID locators to pages.py for the UrbanRoutesPage class.
4. Creating all necessary methods within the UrbanRoutesPage class.
5. Writing the test scripts in main.py calling the methods from pages.py to run the tests and complete the test program.
