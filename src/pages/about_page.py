from selenium.webdriver.common.by import By

from ..elements.base_element import BaseWebElement
from .base_page import BasePage


class About(BasePage):
    @property
    def image_1(self) -> BaseWebElement:
        return BaseWebElement(
            locator="//img[@alt='Разрабатываем систему СБИС']",
            name="Разрабатываем систему СБИС",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def image_2(self) -> BaseWebElement:
        return BaseWebElement(
            locator="//img[@alt='Продвигаем сервисы']",
            name="Продвигаем сервисы",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def image_3(self) -> BaseWebElement:
        return BaseWebElement(
            locator="//img[@alt='Создаем инфраструктуру']",
            name="Создаем инфраструктуру",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def image_4(self) -> BaseWebElement:
        return BaseWebElement(
            locator="//img[@alt='Сопровождаем клиентов']",
            name="Сопровождаем клиентов",
            driver=self.driver,
            by=By.XPATH,
        )
