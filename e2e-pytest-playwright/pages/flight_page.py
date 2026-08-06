from pages.abstract_page import AbstractPage

class FlightPage(AbstractPage):
  
  def select_oneway_trip(self):
    self.page.locator("xpath=//input[@name='tripType' and @value='oneway']").click()

  def select_return_trip(self):
    self.page.locator("xpath=//input[@name='tripType' and @value='return']").click()


  def select_depart_from(self, city):
    self.page.select_option("select[name='fromPort']", label=city)

  def select_arrive_at(self, city):
    self.page.select_option("select[name='toPort']", label=city)

  def select_departure_day(self, day):
    self.page.select_option("#departDay", label=day)

  def select_departure_month(self, month_year):
    self.page.select_option("#departMonth", label=month_year)

  def select_return_day(self, day):
    self.page.select_option("#returnDay", label=day)

  def select_return_month(self, month_year):
    self.page.select_option("#returnMonth", label=month_year)
    
  def click_continue(self):
    self.page.locator("xpath=//input[@value='Continue']").click()
