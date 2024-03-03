import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrom_options = webdriver.ChromeOptions()
        chrom_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrom_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    request.cls.driver = driver
    yield
    driver.close()

