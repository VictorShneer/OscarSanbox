
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es or ru or fr or smth")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    # for Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()