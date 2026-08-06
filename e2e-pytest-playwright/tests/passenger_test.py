from playwright.sync_api import Page, expect

from abstract_test import AbstractTest
from test_helper import TestHelper
from pages import *

class TestPassenger(AbstractTest):

  # before(:all)
  @classmethod
  def setup_class(cls):
    super().setup_class()
    cls.page.goto(TestHelper.site_url())
    
  def test_can_enter_passenger_details(self):
    page = self.page

    self.sign_in("agileway", "test$W1se")

    flight_page = FlightPage(self.driver) # or self.page
    flight_page.select_oneway_trip()
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")
    flight_page.select_departure_day("02")
    flight_page.select_departure_month("May 2026")
    flight_page.click_continue()

    passenger_page = PassengerPage(self.page)
    passenger_page.enter_first_name("Bob")
    passenger_page.enter_last_name("Tester")
    passenger_page.click_next()

    # Verify holder name
    expect(page.locator("input[name='holder_name']")).to_have_value( "Bob Tester")
