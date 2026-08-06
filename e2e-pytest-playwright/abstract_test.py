import time
import datetime
import sys
import os
import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from test_helper import TestHelper

# Pytest may run them in the same process, and Playwright Sync API does not like being started multiple times inside an existing async environment.

_playwright = None

class AbstractTest(TestHelper):
    
  @classmethod
  def setup_class(cls):
    # before(:all)
    global _playwright
    print("Starting a new test...", cls.__name__)
    
    if _playwright is None:
      _playwright = sync_playwright().start()

    cls.playwright = _playwright

    cls.browser = cls.open_browser()
    #if browser_name == "firefox":
      #cls.browser = cls.playwright.firefox.launch(headless=headless)
    #elif browser_name == "webkit":
      #cls.browser = cls.playwright.webkit.launch(headless=headless)
    #else:
      #print("Starting a new Chromium browser")
      #cls.browser = cls.playwright.chromium.launch(headless=headless)

    cls.context = cls.browser.new_context()
    cls.page = cls.context.new_page()

  # after(:all)
  @classmethod
  def teardown_class(cls):
    # if running individual test case via TestWise, keep browser (and Playwright Inspector)
    if TestHelper.is_debugging():
      cls.puts("Test execution completes, keep browser open for inspection")
      cls.page.pause();
      
    cls.context.close()
    cls.browser.close()
    
    # Stop Playwright only once
    global _playwright

    if _playwright is not None:
      _playwright.stop()
      _playwright = None

   
  # Alias 'driver' -> 'page'. This make WebDriver test transit over easier 
  @property
  def driver(self) -> Page:
        return self.page

