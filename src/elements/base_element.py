from typing import Callable, Union

import allure
from selenium.webdriver import ActionChains, Remote
from selenium.webdriver.remote.webelement import By, WebElement
from selenium.webdriver.support import expected_conditions as ec

from src.cases import step
from src.elements.utils import WebWait


class BaseWebElement:
    """
    Базовый Элемент
    :param locator: Локатор элемента
    :param driver: Веб драйвер
    :param by: Способ поиска элемента
    :param timeout: Максимальное время (секунды) ожидание элемента
    :param _element: Элемент
    """

    timeout: int = 15

    def __init__(
        self,
        locator: str,
        name: str,
        driver: Union[Remote, WebElement],
        by: str = By.ID,
    ) -> None:
        self.by = by
        self.locator = locator
        self.name = name
        self.driver = driver
        self._element = self._get_element()

    def condition(self) -> Callable[[Remote], str]:
        """Возвращает фкункцию проверки состояния"""
        return ec.presence_of_element_located((self.by, self.locator))

    def get_attribute(self, value: str = "disabled") -> str:
        """Получить значение атрибута"""
        return self._element.get_attribute(value)

    def get_property(self, value: str = "disabled") -> str | bool | WebElement | dict:
        """Получить значение атрибута"""
        return self._element.get_property(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def _get_locator(self, locator: str) -> str:
        """
        Проверяет от чего идет поиск элемента, при необходимости форматирует локатор
        :param locator: Локатор эелемента
        """
        if isinstance(self.driver, WebElement) and not locator.startswith("."):
            return f".{locator}"
        return locator

    def _get_element(self) -> WebElement:
        """Поиск элемента с ожиданием"""
        return WebWait(driver=self.driver, timeout=self.timeout).until(
            method=self.condition(),
            message=f"Not found element: {self}({self.locator})",
        )


class Button(BaseWebElement):
    """Базовый класс кнопки"""

    @property
    def get_button(self) -> WebElement:
        """Возвращает элемент"""
        return self._element

    def text(self) -> str:
        """Возвращает текст элемента"""
        return self._element.text

    def click(self) -> None:
        """Клик по элементу"""

        with allure.step(f"Нажать на кнопку: {self.name}"):
            WebWait(driver=self.driver, timeout=self.timeout).until(
                ec.element_to_be_clickable((self.by, self.locator)),
            )
            return self._element.click()

    def move_and_click(self) -> None:
        with allure.step(f"Нажать на кнопку: {self.name}"):
            ActionChains(self.driver).move_to_element(self._element).perform()
            return self._element.click()


class Text(BaseWebElement):
    """Базовый класс текст"""

    def text(self) -> str:
        """Возвращает текст элемента"""
        return self._element.text

    def click(self) -> None:
        """Клик по элементу"""
        self._element.click()
