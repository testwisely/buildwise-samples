from playwright.sync_api import Page, expect

from abstract_test import AbstractTest
from test_helper import TestHelper
from pages import *

class TestFlights(AbstractTest):

  # before(:all)
  @classmethod
  def setup_class(cls):
    super().setup_class()
    cls.page.goto(TestHelper.site_url())
    TestHelper.sign_in(cls, "agileway", "test$W1se")
    
  # before(:each)
  def setup_method(self):
    self.page.goto(TestHelper.site_url() + "/flights/start")

  def test_one_way_trip(self):
    page = self.page
    flight_page = FlightPage(self.page)
    flight_page.select_oneway_trip()
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")
    flight_page.select_departure_day("02")
    flight_page.select_departure_month("May 2026")
    flight_page.click_continue()
    expect(page.locator("body")).to_contain_text("2026-05-02 Sydney to New York")
    

  def test_return_trip(self):
    page = self.page
    flight_page = FlightPage(self.page)
    flight_page.select_return_trip()
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")
    flight_page.select_departure_day("02")
    flight_page.select_departure_month("May 2026")
    flight_page.select_return_day("04")
    flight_page.select_return_month("June 2026")
    flight_page.click_continue()
    expect(page.locator("body")).to_contain_text("2026-05-02 Sydney to New York")
    assert "2026-06-04 New York to Sydney" in self.page_text()
