# require 'rubygems'
gem "appium_lib"

require "appium_lib"
require "rspec"

# include utility functions such as 'page_text', 'try_for', 'fail_safe', ..., etc.
require "#{File.dirname(__FILE__)}/agileway_utils.rb"

# this loads defined page objects under pages folder
require "#{File.dirname(__FILE__)}/pages/abstract_page.rb"
Dir["#{File.dirname(__FILE__)}/pages/*_page.rb"].each { |file| load file }
Dir["#{File.dirname(__FILE__)}/pages/*_window.rb"].each { |file| load file }
Dir["#{File.dirname(__FILE__)}/pages/*_dialog.rb"].each { |file| load file }


# This is the helper for your tests, every test file will include all the operation
# defined here.
module TestHelper
  include AgilewayUtils
  if defined?(TestWiseRuntimeSupport)
    include TestWiseRuntimeSupport
  end

  def driver
    @driver
  end
  
  def app_id
    'xxx'
  end
  
  def appium_opts
    app_file = File.join(File.dirname(__FILE__), "app", "calculator-fdroid-release.apk")
    
    # matching your emulator's system version
    platform_version = ENV["ANDROID_PLATFORM_VERSION"] || "15"
    
    # matching your emulator name, by running 'adb devices'
    device_name = ENV["ANDROID_DEVICE_NAME"] || "emulator-5554"
    
    opts = {
      caps: {
        automationName: 'UiAutomator2',
        platformName: 'Android',
        platform: 'Android',
        platformVersion: platform_version,      
        deviceName: device_name,  
        app: app_file,
        appPackage: 'com.simplemobiletools.calculator',
        appActivity: 'com.simplemobiletools.calculator.activities.SplashActivity.Orange'
      },
      appium_lib: {
        server_url: "http://127.0.0.1:4723"
      },
    }
  end

  def debugging?
    if ENV["RUN_IN_TESTWISE"].to_s == "true" && ENV["TESTWISE_RUNNING_AS"] == "test_case"
      return true
    end
    return $TESTWISE_DEBUGGING && $TESTWISE_RUNNING_AS == "test_case"
  end
  
  # quick to refer the test data file under 'testdata' folder
  def test_data_file(relative_path)
    the_file = File.expand_path File.join(File.dirname(__FILE__), "testdata", relative_path)
    the_file.gsub!("/", "\\") if RUBY_PLATFORM =~ /mingw/
    return the_file
  end

  # quick to refer tmp file under 'tmp' folder
  def tmp_dir(sub_dir_name, opts = {})
    the_dir = File.expand_path File.join(File.dirname(__FILE__), "tmp", sub_dir_name)
    the_dir.gsub!("/", "\\") if RUBY_PLATFORM =~ /mingw/
    unless opts[:do_not_create]
      FileUtils.mkdir_p(the_dir) unless Dir.exist?(the_dir)
    end
    return the_dir
  end
	
  # prevent extra long string generated test scripts that blocks execution when running in
  # TestWise or BuildWise Agent
  def safe_print(str)
    return if str.nil? || str.empty?
    if (str.size < 250)
      puts(str)
      return
    end

    if ENV["RUN_IN_TESTWISE"].to_s == "true" && ENV["RUN_IN_BUILDWISE_AGENT"].to_s == "true"
      puts(str[0..200])
    end
  end
  
  # a convenient method to use main_window, if @main_window is set 
  def main_window
    @main_window
  end
  
  # a convenient method to use main_window, extract function refactoring support use this
  #  driver.find_element(...), after extraction => win.find_element
  # this way, test execution can still run faster in debugging mode (attach session)
  def win
    @main_window
  end
  
end

