from playwright.sync_api import Page, expect

from abstract_test import AbstractTest
from test_helper import TestHelper
from pages import *

class TestPayment(AbstractTest):

  # before(:all)
  @classmethod
  def setup_class(cls):
    super().setup_class()
    cls.page.goto(TestHelper.site_url())
    
  # before each
  def setup_method(self):      
    # pass
    self.sign_in("agileway", "test$W1se")

    flight_page = FlightPage(self.page)
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
    
  def test_get_booking_confirmation_after_payment(self):
    page = self.page
    payment_page = PaymentPage(self.page)
    payment_page.select_card_type_master()
    payment_page.enter_holder_name("Bob the Tester")
    payment_page.enter_card_number("4242424242424242")
    payment_page.select_expiry_month("04")
    payment_page.select_expiry_year("2029")
    payment_page.click_pay_now()
    
    expect(page.locator("body")).to_contain_text("Booking number")

    booking_number = page.locator("#booking_number").inner_text()
    print(f"Booking number: {booking_number}")
