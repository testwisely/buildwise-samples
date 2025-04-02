load File.dirname(__FILE__) + "/../test_helper.rb"

# don't use selenium excessive log directly when running in TestWise
# if you want do, use the statement below, and run the test from command line to see debug log
#
# Selenium::WebDriver.logger.level = :debug unless defined?(TestWiseRuntimeSupport)

describe "User Login" do
  include TestHelper

  before(:all) do
    @driver = $driver = Selenium::WebDriver.for(browser_type, browser_options)
    driver.manage().window().resize_to(1280, 720)
    driver.manage().window().move_to(30, 78)
    driver.get(site_url)
  end

  after(:all) do
    driver.quit unless debugging?
  end
  
  before(:each) do
    visit("/login")
  end

  it "[1] Can sign in OK" do
    login("agileway", "testwise")
    sleep 0.1
    expect(driver.find_element(:id, "flash_notice").text).to eq("Signed in!")
    driver.find_element(:link_text, "Sign off (agileway)").click
  end

  it "[1] User failed to sign in due to invalid password", :tag => "showcase" do    
    login_page = LoginPage.new(driver)
    login_page.login("agileway", "badpass")
    sleep 0.1
    expect(driver.page_source).to include("Invalid email or password")
  end
end
