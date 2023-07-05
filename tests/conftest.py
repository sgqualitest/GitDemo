import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.service import Service

# This is predefined method to get value from cmd. Refer https://docs.pytest.org/en/7.1.x/example/simple.html
# --browser_name is the parameter which is passed in cmd
# action will be to store browser name from cmd
# default is chrome, if no browser name is passed in cmd then it will pick chrome
# generate html report : run the command in cmd: py.test --html=report.html
driver = None  # global driver declared as None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# for cmd: py.test --browser_name firefox
@pytest.fixture(
    scope="class")  # scope="class": this will be executed only once before a class is called. In our case it is used in test_e2e file
def setup(request):
    global driver  # driver intialized below will be set as global
    browser = request.config.getoption("--browser_name")  # To get name of the browser from pytest_addoption method
    if browser == "chrome":
        service_obj = Service("C:/Users/shyam.gorasia/Documents/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "firefox":
        service_obj = Service("C:/Users/shyam.gorasia/Documents/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser == "ie":
        print("IE")

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver  # Now the driver is assigned to class level driver request parameter(request.cls.driver)
    yield
    driver.close()


@pytest.mark.hookwrapper  # this piece of code is required to generate html report
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)