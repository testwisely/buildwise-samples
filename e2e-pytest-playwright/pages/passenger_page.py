from pages.abstract_page import AbstractPage

class PassengerPage(AbstractPage):

  def enter_first_name(self, first_name):
    self.page.locator("input[name='passengerFirstName']").fill(first_name)

  def enter_last_name(self, last_name):
    self.page.locator("input[name='passengerLastName']").fill(last_name)

  def click_next(self):
    self.page.locator("xpath=//input[@value='Next']").click()


