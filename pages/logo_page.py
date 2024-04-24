import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.logo import LocatorLogoPage
from locators.zakaz_samokat import LocatorZakazSamokat
from pages.base_page import BasePage
from pages.order_samokat import OrderSamokat
from urls import Ursl


class LogoPage(BasePage):


    @allure.step("Проверка на сайт ЯндексДзен")
    def dzen(self):
        self.driver.find_element(*LocatorLogoPage.YANDEX_LOGO).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(Ursl.DZEN_URL))
        return self.driver.current_url


    @allure.step("Возврат на главную страницу при нажатии лого 'Самокат'")
    def logo_samokat(self):
        self.driver.find_element(*LocatorZakazSamokat.HEADER_ZAKAZAT).click()
        kurl = self.driver.current_url
        self.driver.find_element(*LocatorLogoPage.SAMOKAT_LOGO).click()
        return kurl


