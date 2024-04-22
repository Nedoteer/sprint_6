import allure

from pages.logo_page import LogoPage


class TestLogoPage:

    @allure.title("Проверка лого")
    def test_logo_page(self, driver):
        logo_page = LogoPage(driver)
        url = logo_page.url_samokat()
        assert logo_page.dzen() == url

    @allure.title("Проверка Логотипа Яндекс в новом окне, клик возвращает на главную страницу")
    def test_logo_samokat(self, driver):
        logo_page = LogoPage(driver)
        main = logo_page.url_samokat()
        assert logo_page.logo_samokat() != main