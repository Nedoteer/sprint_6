import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.enjoy_samokat import EnjoySamokat


class LogoPage(BasePage):
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    HOME_LOGO = (By.XPATH, "//div[@class = 'Home_Header__iJKdX']")

    @allure.step("Проверка на сайт ЯндексДзен")
    def dzen(self):
        self.driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes('https://dzen.ru/?yredirect=true'))
        return self.driver.current_url


    @allure.step("Возврат на главную страницу при нажатии лого 'Самокат'")
    def logo_samokat(self):
        self.driver.find_element(*EnjoySamokat.HEADER_ZAKAZAT).click()
        kurl = self.driver.current_url
        self.driver.find_element(By.CLASS_NAME, "Header_LogoScooter__3lsAR").click()
        return kurl


    @allure.step("Получение урл")
    def url_samokat(self):
        return self.driver.current_url
