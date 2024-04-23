from selenium.webdriver.common.by import By


class LocatorZakazSamokat:

    HEADER_ZAKAZAT = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    HEADER_ZAKAZAT2 = (By.XPATH, "//button[@class =Button_Button__ra12g Button_UltraBig__UU3Lp")
    NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    FAMILYA = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADRES = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO1 = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    METRO_STANTION1 = (By.XPATH, "//div[contains(text(), 'Сокольники')]")
    METRO2 = (By.XPATH, "//input[@placeholder = '*  Станция метро']")
    METRO_STANTION2 = (By.XPATH, "//div[contains(text(), 'Красносельская')]")
    PHONE = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    ENTER = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    VOPROS_DOSTAVKI = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    VIBOR_DATI = (By.XPATH, "//div[@aria-label = 'Choose четверг, 11-е апреля 2024 г.']")
    SROK = (By.XPATH, "//div[@class = 'Dropdown-placeholder']")
    SUTKI = (By.XPATH, "//div[contains(text(), 'двое суток')]")
    ZAKAZAT = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    KNOPKA_DA = (By.XPATH, "//button[contains(text(), 'Да')]")
    DONE = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
