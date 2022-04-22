import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# передача аргументов через командную строку
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: english or russian")
    

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
