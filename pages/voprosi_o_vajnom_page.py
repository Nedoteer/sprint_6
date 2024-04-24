
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
        new_locator = self.changest_loc(VoprosiOVajnom.otvet, i)
        new_otvet = self.changest_loc(VoprosiOVajnom.vopros, i)
        self.driver.find_element(*new_otvet).click()
        otveti = self.driver.find_element(*new_locator).text
        return otveti


    @allure.step('Нажатие на куки')
    def click_cockie(self):
        self.driver.find_element(*VoprosiOVajnom.KUKI).click()

    @allure.step('Преображение локатора')
    def changest_loc(self, locator, i):
        b,l = locator
        res = l.replace('0', f'{i}')
        new = [b, res]
        return new