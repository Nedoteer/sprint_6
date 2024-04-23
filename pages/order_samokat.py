import allure
from selenium.webdriver.common.by import By

from locators.zakaz_samokat import LocatorZakazSamokat
from pages.base_page import BasePage

class OrderSamokat(BasePage):

    @allure.step("Заполнение формы заказа")
    def set_input(self, name, familya, adres, phone):
        self.driver.find_element(*LocatorZakazSamokat.NAME).send_keys(name)
        self.driver.find_element(*LocatorZakazSamokat.FAMILYA).send_keys(familya)
        self.driver.find_element(*LocatorZakazSamokat.ADRES).send_keys(adres)
        self.driver.find_element(*LocatorZakazSamokat.METRO1).click()
        self.driver.find_element(*LocatorZakazSamokat.METRO_STANTION1).click()
        self.driver.find_element(*LocatorZakazSamokat.PHONE).send_keys(phone)
        self.driver.find_element(*LocatorZakazSamokat.ENTER).click()
        self.driver.find_element(*LocatorZakazSamokat.VOPROS_DOSTAVKI).click()
        self.driver.find_element(*LocatorZakazSamokat.VIBOR_DATI).click()
        self.driver.find_element(*LocatorZakazSamokat.SROK).click()
        self.driver.find_element(*LocatorZakazSamokat.SUTKI).click()
        self.driver.find_element(*LocatorZakazSamokat.ZAKAZAT).click()
        self.driver.find_element(*LocatorZakazSamokat.KNOPKA_DA).click()
        return self.driver.find_element(*LocatorZakazSamokat.DONE).text



    @allure.step("Сценарий нажатия кнопки вверху экрана")
    def button_one(self):
        self.driver.find_element(By.XPATH, "//button[@class = 'Button_Button__ra12g']").click()


    @allure.step("Сценарий нажатия кнопки, снизу экрана")
    def button_two(self):
        self.click_cockie()
        self.driver.find_element(By.XPATH, "//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']").click()


    @allure.step("Нажатие кнопки куки")
    def click_cockie(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'да все привыкли')]").click()