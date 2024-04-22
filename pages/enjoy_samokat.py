import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage

class EnjoySamokat(BasePage):
    HEADER_ZAKAZAT = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    HEADER_ZAKAZAT2 = (By.XPATH, "//button[@class =Button_Button__ra12g Button_UltraBig__UU3Lp")
    NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    FAMILYA = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADRES = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO1 = (By.XPATH, "//input[@placeholder = '*  Станция метро']")
    METRO_STANTION1 = (By.XPATH, "//div[contains(text(), 'Сокольники')]")
    METRO2 = (By.XPATH, "//input[@placeholder = '*  Станция метро']")
    METRO_STANTION2 = (By.XPATH, "//div[contains(text(), 'Красносельская')]")
    PHONE = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    ENTER = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    VOPROS_DOSTAVKI = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    VIBOR_DATI = (By.XPATH, "//div[@aria-label = 'Choose четверг, 11-е апреля 2024 г.']")
    SROK = (By.XPATH, "//input[@placeholder = '* Срок аренды']")
    SUTKI = (By.XPATH, "//div[@class = 'Dropdown-placeholder is-selected']")
    ZAKAZAT = (By.XPATH, "//input[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    KNOPKA_DA = (By.XPATH, "//button[contains(text(), 'Да')]")
    DONE = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")

    @allure.step("Заполнение формы заказа")
    def set_input(self, name, familya, adres, phone):
        self.driver.find_element(By.XPATH, "//input[@placeholder = '* Имя']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@placeholder = '* Фамилия']").send_keys(familya)
        self.driver.find_element(By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']").send_keys(adres)
        self.driver.find_element(By.XPATH, "//input[@placeholder = '* Станция метро']").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Сокольники')]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']").send_keys(phone)
        self.driver.find_element(By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder = '* Когда привезти самокат']").click()
        self.driver.find_element(By.XPATH, "//div[@aria-label = 'Choose четверг, 11-е апреля 2024 г.']").click()
        self.driver.find_element(By.XPATH, "//div[@class = 'Dropdown-placeholder']").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'двое суток')]").click()
        self.driver.find_element(By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Да')]").click()
        return self.driver.find_element(By.XPATH, "//button[contains(text(), 'Посмотреть статус')]").text


    @allure.step("Сценарий первой кнопки вверху экрана")
    def button_one(self):
        self.driver.find_element(By.XPATH, "//button[@class = 'Button_Button__ra12g']").click()


    @allure.step("Сценарий второй кнопки, снизу экрана")
    def button_two(self):
        self.click_cockie()
        self.driver.find_element(By.XPATH, "//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']").click()


    @allure.step("Нажатие кнопки куки")
    def click_cockie(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'да все привыкли')]").click()