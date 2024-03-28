from selenium.webdriver.common.by import By

from ..elements.base_element import Button
from .base_page import BasePage


class RegionPopUp(BasePage):
    @property
    def kamchatka_button(self) -> Button:
        return Button(
            locator="//*[text()='41 Камчатский край']",
            name="Контакты",
            driver=self.driver,
            by=By.XPATH,
        )
