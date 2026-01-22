load File.dirname(__FILE__) + '/../test_helper.rb'

describe "Select Flights" do
  include TestHelper

  before(:all) do
    use_current_browser
    
    driver.get(site_url)
    fail_safe{ visit("/sign_out")  }
    
        login_page = LoginPage.new(driver)
    login_page.login("agileway", "test$W1se")
  end

  after(:all) do
  end
  
  before(:each) do
    visit("/")
    sleep 1 # for some webdriver verson, it might not wait page loaded
  end

  it "[3] Return trip" do
    flight_page = FlightPage.new(driver)
    flight_page.select_trip_type("return")
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")

    flight_page.select_depart_day("02")
    flight_page.select_depart_month("May 2027")
    flight_page.select_return_day("04")
    flight_page.select_return_month("June 2027")
    flight_page.click_continue

    try_for(2) { expect(page_text).to include("2027-05-02 Sydney to New York") }
    expect(page_text).to include("2027-06-04 New York to Sydney")
  end

  it "[2] One-way trip" do
    flight_page = FlightPage.new(driver)
    flight_page.select_trip_type("oneway")
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")

    flight_page.select_depart_day("02")
    flight_page.select_depart_month("May 2027")
    flight_page.click_continue

    try_for(2) { expect(page_text).to include("2027-05-02 Sydney to New York") }
  end


end
