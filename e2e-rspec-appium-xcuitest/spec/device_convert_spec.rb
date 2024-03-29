load File.dirname(__FILE__) + "/../test_helper.rb"

describe "Convert" do
  include TestHelper

  before(:all) do
    @driver = Appium::Driver.new(device_opts()).start_driver
  end

  after(:all) do
    @driver.quit unless debugging?
  end
  
  it "Convert a new amount" do    
    elem_input = driver.find_element(:xpath, "//XCUIElementTypeApplication[@name=\"iCurrency\"]//XCUIElementTypeTextField")
    elem_input.clear
    elem_input.send_keys("50")
    elem_convert = driver.find_element :name, "Convert"
    elem_convert.click
    sleep 0.2
    puts("Checking")
    elem_euro_sign = driver.find_element(:name, "€")
    puts "found elem_euro_sign"
    
    # try Xpath on http://xpather.com/
    elem_euro_amount = driver.find_element(:xpath, "//XCUIElementTypeApplication[@name='iCurrency']//XCUIElementTypeStaticText[@name='€']/following-sibling::XCUIElementTypeStaticText[position()=1]")
    new_euro_amount = elem_euro_amount.text.to_f
    expect(new_euro_amount).to be < 50  
  end
end
