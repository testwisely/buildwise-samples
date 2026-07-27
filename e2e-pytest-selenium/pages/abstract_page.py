from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AbstractPage(object):

  def __init__(self, driver):
    self.driver = driver
