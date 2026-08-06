from playwright.sync_api import Page, expect
import time

from abstract_test import AbstractTest
from test_helper import TestHelper
from pages import *

class TestLogin(AbstractTest):
  
  # before(:all)
  @classmethod
  def setup_class(cls):
    super().setup_class()
  
  # before(:each)
  def setup_method(self):
    self.driver.goto(TestHelper.site_url())

  def test_user_can_sign_in_ok(self):
    page = self.page
    self.sign_in("agileway", "test$W1se")
    expect(page.locator("body")).to_contain_text("Welcome agileway")
    self.sign_out()
    time.sleep(0.5)
    
  def test_user_failed_to_sign_in_due_to_invalid_password(self):
    page = self.page
    self.sign_in("agileway", "badpass")
    expect(page.locator("body")).to_contain_text(
    "Invalid email or password")

  def test_admin_user_can_sign(self):
    page = self.page
    self.sign_in("admin", "secret")
    expect(page.get_by_role("link", name="Administration")).to_be_visible()
    self.sign_out()
