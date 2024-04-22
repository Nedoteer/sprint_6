
import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class VoprosiOVafnom(BasePage):
    VOPROS1 = (By.ID, "accordion__heading-0")
    OTVET_VOPROS1 = (By.ID, "accordion__panel-0")
    VOPROS2 = (By.ID, "accordion__heading-1")
    OTVET_VOPROS2 = (By.ID, "accordion__panel-1")
    VOPROS3 = (By.ID, "accordion__heading-2")
    OTVET_VOPROS3 = (By.ID, "accordion__panel-2")
    VOPROS4 = (By.ID, "accordion__heading-3")
    OTVET_VOPROS4 = (By.ID, "accordion__panel-3")
    VOPROS5 = (By.ID, "accordion__heading-4")
    OTVET_VOPROS5 = (By.ID, "accordion__panel-4")
    VOPROS6 = (By.ID, "accordion__heading-5")
    OTVET_VOPROS6 = (By.ID, "accordion__panel-5")
    VOPROS7 = (By.ID, "accordion__heading-6")
    OTVET_VOPROS7 = (By.ID, "accordion__panel-6")
    VOPROS8 = (By.ID, "accordion__heading-7")
    OTVET_VOPROS8 = (By.ID, "accordion__panel-7")


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
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'да все привыкли')]").click()
