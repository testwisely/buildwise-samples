load File.dirname(__FILE__) + '/../test_helper.rb'

describe "Start the browser" do
  include TestHelper

  before(:all) do
    $CHROME_NEW_INSTANCE = true # start a new browser 
    @driver = $driver = Selenium::WebDriver.for(browser_type, browser_options)
    @driver.get(site_url)
  end

  after(:all) do
    # don't close it
    # @driver.quit unless debugging?
  end

  it "Launch the browser, use this one later" do
    
  end

end
