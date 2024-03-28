from selenium.webdriver.common.by import By

from ..elements.base_element import Button
from .base_page import BasePage


class Tensor(BasePage):
    @property
    def about_button(self) -> Button:
        return Button(
            locator="//div[@class='tensor_ru-Index__block4-bg']//*[text()='Подробнее']",
            name="Подробнее",
            driver=self.driver,
            by=By.XPATH,
        )
