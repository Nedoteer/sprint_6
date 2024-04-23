
import allure
from selenium.webdriver.common.by import By

from locators.voprosi import VoprosiOVajnom
from pages.base_page import BasePage


class VoprosiOVafnom(BasePage):



    @allure.step('Скрол страницы до вопросов')
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 3460)")

    @allure.step('Выбор вопросов и получение ответов')
    def set_voprosi(self, i):
        self.click_cockie()
        self.scroll()
        vopros = (By.ID, f"accordion__heading-{i}")
        otvet = (By.ID, f"accordion__panel-{i}")
        self.driver.find_element(*vopros).click()
        otveti = self.driver.find_element(*otvet).text
        return otveti


    @allure.step('Нажатие на куки')
    def click_cockie(self):
        self.driver.find_element(*VoprosiOVajnom.KUKI).click()
