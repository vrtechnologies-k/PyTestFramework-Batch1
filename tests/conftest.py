import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="Invocation the browser"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser-name")
    if browser == "chrome":
        s = Service(executable_path="c:\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)

    elif browser == "firefox":
        s = Service(executable_path="c:\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    elif browser == "ie":
        s = Service(executable_path="c:\\IEDriverServer.exe")
        driver = webdriver.ie(service=s)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver  # Up to here precondition
    yield
    driver.quit()  # post condition
