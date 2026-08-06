from pages.abstract_page import AbstractPage

class LoginPage(AbstractPage):

  def enter_username(self, user):
    self.page.fill("#username", user)
 
  def enter_password(self, password):
    self.page.fill("#password", password)

  def click_sign_in(self):
    self.page.click("input:has-text('Sign in')")
    