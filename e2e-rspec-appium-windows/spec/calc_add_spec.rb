load File.dirname(__FILE__) + "/../test_helper.rb"

describe "Calculator on Windows POM" do
  include TestHelper

  before(:all) do
    @driver = $driver = if Appium::VERSION.to_i >= 12
        Appium::Driver.new(appium2_opts()).start_driver
      else
        Appium::Driver.new(app_caps, true).start_driver
      end
  end

  after(:all) do
    driver.quit unless debugging?
  end

  it "Single digit" do
    main_window = MainWindow.new(driver, "Calculator")
    main_window.click_number("Four")
    main_window.click_plus
    main_window.click_number("Three")
    main_window.click_equals
    expect( main_window.result).to eq("Display is 7")
  end
end
