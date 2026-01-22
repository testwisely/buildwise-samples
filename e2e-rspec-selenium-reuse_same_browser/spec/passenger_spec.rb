load File.dirname(__FILE__) + '/../test_helper.rb'

describe "Passenger" do
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
  

  it "[4] Can enter passenger details (using page objects)" do
    flight_page = FlightPage.new(driver)
    try_for(2) { flight_page.select_trip_type("return") }
    flight_page.select_depart_from("Sydney")
    flight_page.select_arrive_at("New York")

    flight_page.select_depart_day("02")
    flight_page.select_depart_month("May 2027")
    flight_page.select_return_day("04")
    flight_page.select_return_month("June 2027")
    flight_page.click_continue

    # now on passenger page
    passenger_page = PassengerPage.new(driver)
    try_for(2) { passenger_page.click_next }
    expect(page_text).to include("Must provide last name")
    passenger_page.enter_first_name("Bob")
    passenger_page.enter_last_name("Tester")
    passenger_page.click_next

    # If assertion text is "Wendy", the test will fail. 
    # To fix it, change the step below fails: "Wendy" => "Bob"
    expect(driver.find_element(:name, "holder_name").attribute("value")).to eq("Bob Tester")
  end

end

