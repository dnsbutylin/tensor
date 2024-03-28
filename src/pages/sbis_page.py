from selenium.webdriver.common.by import By

from ..elements.base_element import Button
from .base_page import BasePage


class Sbis(BasePage):
    @property
    def contacts_button(self) -> Button:
        return Button(
            locator="//*[text()='Контакты']",
            name="Контакты",
            driver=self.driver,
            by=By.XPATH,
        )
