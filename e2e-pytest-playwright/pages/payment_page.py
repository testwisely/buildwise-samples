from pages.abstract_page import AbstractPage

class PaymentPage(AbstractPage):

  def select_card_type_master(self):
    self.page.locator("xpath=//input[@name='card_type' and @value='master']").click()

  def enter_holder_name(self, name):
    self.page.locator("input[name='holder_name']").fill(name)

  def enter_card_number(self, card_no):
    self.page.locator("input[name='card_number']").fill(card_no)

  def select_expiry_month(self, month):
    self.page.select_option("select[name='expiry_month']", label=month)

  def select_expiry_year(self, year):
    self.page.select_option("select[name='expiry_year']", label=year)

  def click_pay_now(self):
    self.page.locator("xpath=//input[@type='submit' and @value='Pay now']").click()
