import os
import sys
from selenium.webdriver.common.by import By

# load modules from parent dir, pages will be referred from there too.
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../")
#from pages.login_page import LoginPage

from abstract_test import AbstractTest
from pages import *

class LoginTestCase(AbstractTest):

  @classmethod
  def setUpClass(cls):
    # open_browser method defined in test_helper.py
      cls.driver = cls.open_browser();
      cls.driver.set_window_size(1280, 720)
      cls.driver.set_window_position(30, 78)

      # TODO
      # executor_url = cls.driver.command_executor._url
      session_id = cls.driver.session_id
      # print("WDURL: " + executor_url + ", session id: " + session_id);
      cls.puts("session id: " + session_id) # ", WDURL: " + executor_url + "|");


  @classmethod
  def tearDownClass(cls):
    if not cls.is_debugging():
      cls.driver.quit()
    print("Not quiting");

  def setUp(self):
    self.driver.get(self.site_url())

  def test_sign_in_failed(self):
    # ...
    login_page = LoginPage(self.driver)
    login_page.enter_username("agileway")
    login_page.enter_password("badpass")
    login_page.click_sign_in()
    # self.assertIn("Demo Fail this test case", self.driver.find_element_by_tag_name("body").text)

  def test_sign_in_ok(self):
    # ...
    login_page = LoginPage(self.driver)
    login_page.enter_username("agileway")
    login_page.enter_password("test$W1se")
    login_page.click_sign_in()

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=xmlrunner.XMLTestRunner(output='reports'),
#         failfast=False, buffer=False, catchbreak=False)
