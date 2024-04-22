import allure
import pytest
from pages.enjoy_samokat import EnjoySamokat


class TestEnjoySamokat:

    @allure.title("Позитивный сценарий заказа самоката")
    def test_enjoy_samokat(self, driver):
        name = EnjoySamokat(driver)
        name.button_one()
        assert name.set_input('Фобос', 'Спутник', 'Ленина 6', '+79995552211') == 'Посмотреть статус'

    @allure.title('Второй сценарий заказа по нажатию кнопки "Заказать" внизу')
    def test_enjoy_samokat2(self, driver):
        name = EnjoySamokat(driver)
        name.button_two()
        assert name.set_input('Крисмос', 'Годичный', 'Судоплатовская 1', '+78883331122') == 'Посмотреть статус'