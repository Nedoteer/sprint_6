from selenium.webdriver.common.by import By


class LocatorLogoPage:
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    HOME_LOGO = (By.XPATH, "//div[@class = 'Home_Header__iJKdX']")