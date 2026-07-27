from pages.abstract_page import AbstractPage
from selenium.webdriver.common.by import By

class LoginPage(AbstractPage):

  def enter_username(self, user):
    self.driver.find_element(By.ID, "username").send_keys(user)
 
  def enter_password(self, password):
    self.driver.find_element(By.ID, "password").send_keys(password)

  def click_sign_in(self):
    self.driver.find_element(By.XPATH, "//input[@value='Sign in']").click()
