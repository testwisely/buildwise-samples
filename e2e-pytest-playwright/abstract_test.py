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
    print("Staring a new test...", cls.__name__)
    
    if _playwright is None:
      _playwright = sync_playwright().start()

    cls.playwright = _playwright

    cls.browser = cls.open_browser() # defined in TestHelper

    cls.context = cls.browser.new_context()
    
    # for view tracer
    if os.environ.get("PLAYWRIGHT_TRACING") == "on":
      print("Playwright tracing enabled")

      os.makedirs("test-results", exist_ok=True)

      cls.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
      )
    
    cls.page = cls.context.new_page()

  # after(:all)
  @classmethod
  def teardown_class(cls):
    # if running individual test case via TestWise, keep browser (and Playwright Inspector)
    if TestHelper.is_debugging():
      cls.puts("Test execution completes, keep browser open for inspection")
      cls.page.pause();
    
    # for view tracer
    if os.environ.get("PLAYWRIGHT_TRACING") == "on":
      cls.context.tracing.stop(path="test-results/trace.zip")
    
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

