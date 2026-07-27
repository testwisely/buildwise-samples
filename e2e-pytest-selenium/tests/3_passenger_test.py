import os
import sys
import time

from selenium.webdriver.common.by import By

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../")
from test_helper import TestHelper

from abstract_test import AbstractTest
from pages import *

class PassengerTestCase(AbstractTest):

  @classmethod
  def setUpClass(cls):
    # open_browser method defined in test_helper.py
    cls.driver = cls.open_browser();
    cls.driver.set_window_size(1280, 720)
    cls.driver.set_window_position(30, 78)

    cls.driver.get(cls.site_url())
    login_page = LoginPage(cls.driver)
    login_page.enter_username("agileway")
    login_page.enter_password("test$W1se")
    login_page.click_sign_in()

  def test_enter_passenger_details(self):
    flight_page = FlightPage(self.driver)
    flight_page.select_trip_type("oneway")
    flight_page.select_depart_from("New York")
    flight_page.select_arrive_at("Sydney")
    flight_page.select_depart_day("04")
    flight_page.select_depart_month("March 2027")
    flight_page.click_continue()

    time.sleep(1)
    passenger_page = PassengerPage(self.driver)
    passenger_page.enter_first_name("Bob")
    passenger_page.enter_last_name("Tester")
    passenger_page.click_next()

    # purposely assertion failure if Wendy
    self.assertEqual("Bob Tester", self.driver.find_element(By.NAME, "holder_name").get_attribute("value"))

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=xmlrunner.XMLTestRunner(output='reports'),
#         failfast=False, buffer=False, catchbreak=False)
