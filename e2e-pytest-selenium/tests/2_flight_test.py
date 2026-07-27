import os
import sys
import time
from selenium.webdriver.common.by import By

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../")
from test_helper import TestHelper
from abstract_test import AbstractTest
from pages import *

class FlightTestCase(AbstractTest):

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

  def setUp(self):
    self.driver.get(self.site_url())

  def test_select_oneway_flight(self):
    flight_page = FlightPage(self.driver)
    flight_page.select_trip_type("oneway")
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")

    flight_page.select_depart_day("02")
    flight_page.select_depart_month("May 2027")
    flight_page.click_continue

    time.sleep(1)


  def test_select_return_flight(self):
    flight_page = FlightPage(self.driver)
    flight_page.select_trip_type("return")
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")

    flight_page.select_depart_day("02")
    flight_page.select_depart_month("May 2027")
    flight_page.select_return_day("04")
    flight_page.select_return_month("June 2027")
    flight_page.click_continue

    time.sleep(1)

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=xmlrunner.XMLTestRunner(output='reports'),
#         failfast=False, buffer=False, catchbreak=False)
