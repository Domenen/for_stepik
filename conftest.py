import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Выберите язык 'ru', 'en', 'fr'"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")

    if not browser_language:
        raise pytest.UsageError("--language должен быть указан (например, 'ru', 'en', 'fr')")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": browser_language}
    )

    browser = webdriver.Chrome(options=options)
    browser.language = browser_language
    yield browser
    browser.quit()