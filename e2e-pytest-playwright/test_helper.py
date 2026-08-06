# a Mixin alike that include in every test case
import os;
import sys;
import time;

import socket;
import codecs;

from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page

class TestHelper:

  # define the base url for target web site
  
  @classmethod
  def site_url(cls):
    the_site_url = os.environ.get("BASE_URL");
    if not the_site_url:
      the_site_url = "https://travel.agileway.net"
    return the_site_url;
  

  # NOTE: note set up for Playwright yet
    
  # A helper function to return webdriver instance
  #  In other languages, take browser type as parameter, but seem no the case for Python
  @classmethod
  def open_browser(cls):
    env_browser = os.environ.get("TARGET_BROWSER")
    # cls.puts(env_browser)
    headless = False
    if env_browser == "firefox":
      cls.browser = cls.playwright.firefox.launch(headless=headless)
    elif env_browser == "safari":
      cls.browser = cls.playwright.webkit.launch(headless=headless)
    else:
      cls.browser = cls.playwright.chromium.launch(headless=headless)
    
    # save driver session for later to attach it, for much easier debugging test steps
    # TODO cls.save_driver_session()
    return cls.browser

  @classmethod
  def is_debugging(cls):
    if "RUN_IN_TESTWISE" in os.environ and "TESTWISE_RUNNING_AS" in os.environ:
      return os.environ['RUN_IN_TESTWISE'] == "true" and os.environ["TESTWISE_RUNNING_AS"] == "test_case"
    else:
      return False


  @classmethod
  def get_testwise_db_file(cls):
    if 'TESTWISE_DB_FILE' in os.environ and os.path.exists(os.environ["TESTWISE_DB_FILE"]):
      print(os.environ["TESTWISE_DB_FILE"])
      return  os.environ["TESTWISE_DB_FILE"]
    else:
      return None

  @classmethod
  def puts(cls, message):
    print(message)
    cls.connect_to_testwise("OUTPUT", message)


  @classmethod
  def connect_to_testwise(cls, message_type, body):
    if "TESTWISE_TRACE_PORT" in os.environ:
      testwise_port = int(os.environ["TESTWISE_TRACE_PORT"])
    else:
      testwise_port = 7535
    # print("TESTWISE PORT: " + str(testwise_port))

    if len(body) > 4000:
      body = body[0:4000]

    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', testwise_port))
        the_message = message_type + "|" + body
        encoded_bytes = the_message.encode()
        #encoded_bytes = codecs.encode(the_message[0, len(the_message)-1], 'utf-8')
        #encoded_bytes = codecs.encode(the_message, 'utf-8')
        s.sendall(encoded_bytes[0:len(encoded_bytes)-1])
        # data = s.recv(1024)
    except ConnectionRefusedError:
      print("Unable to connect to TestWise")

  ## commonly used generic functions that can be used many test scripts.
  #  e.g. assert "2026-06-04 New York to Sydney" in self.page_text()
  # 
  
  def page_text(self):
    return self.page.locator("body").inner_text();

  def page_html(self):
    return self.page.content()


  # Invoking functions work both ways:
  # * TestHelper.sign_in(cls, "agileway", "test$W1se")
  # * self.sign_in("agileway", "test$W1se")
        
  ## user defined functions
  # 
  # examples
  def sign_in(self, username, password):   
    page = self.page
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("xpath=//input[@value='Sign in']").click()

  def sign_out(self):
    page = self.page 
    page.get_by_role("link", name="Sign off", exact=False).click()