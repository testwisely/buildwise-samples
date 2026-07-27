import unittest
import time
import datetime
import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

# load modules from parent dir, pages will be referred from there too.
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../")
from test_helper import TestHelper
from pages import *

class DebuggingTestCase(unittest.TestCase, TestHelper):

  @classmethod
  def setUpClass(cls):
    cls.driver = cls.reuse_current_browser()

  def test_special(self):
    # self.driver.find_element(By.ID, "username").send_keys("James")
    flight_page = FlightPage(self.driver)
    flight_page.select_trip_type("return")
