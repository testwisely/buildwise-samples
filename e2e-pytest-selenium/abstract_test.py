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

# load modules from parent dir, pages will be referred from there too.
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
from test_helper import TestHelper


class AbstractTest(unittest.TestCase, TestHelper):

  @classmethod
  def setUpClass(cls):
    # open_browser method defined in test_helper.py
    cls.driver = cls.open_browser();  
    cls.driver.set_window_size(1280, 720)

  @classmethod
  def tearDownClass(cls):
    if not cls.is_debugging():
      cls.driver.quit()

  def setUp(self):
    pass
    
