import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):  # This returns the browser value to setup method
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    driver = ""
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver


def pytest_addoption(parser):  # Gets value from CLI/hooks
    parser.addoption("--browser")


############## HTML Report - Pytest ##############

# Hook to add environment details to the HTML report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "Parabank ECommerce",
        "Module Name": "Login",
        "Tester Name ": "Swathi"
    }


# Hook to add/delete environment info in the HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
