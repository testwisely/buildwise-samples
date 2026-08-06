# 'conftest.py' is a special Pytest configuration file. Pytest automatically discovers it and makes its fixtures and configuration available to all test modules in the same directory and its subdirectories.

import os

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=True,
        help="Run browser in headed mode"
    )
    parser.addoption(
        "--target_browser",
        action="store",
        default="chromium",
        help="Browser to use: chromium, firefox, webkit"
    )

def pytest_configure(config):
    os.environ["BROWSER"] = config.getoption("--target_browser")

    if config.getoption("--headless"):
        os.environ["BROWSER_HEADLESS"] = "true"
    else: 
        os.environ["BROWSER_HEADLESS"] = "false"

