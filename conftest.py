import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    mozila_driver = webdriver.Firefox()
    mozila_driver.set_window_size(1920, 1080)
    mozila_driver.get('https://qa-scooter.praktikum-services.ru/')
    yield mozila_driver

    mozila_driver.quit()
