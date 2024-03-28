from selenium.webdriver.common.by import By

from ..elements.base_element import Button
from .base_page import BasePage


class Cookie(BasePage):
    @property
    def tensor_cookie_close_button(self) -> Button:
        return Button(
            locator="//*[contains(@class, 'tensor_ru-CookieAgreement__close')]",
            name="Кнопка крестик на куках",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def sbis_cookie_close_button(self) -> Button:
        return Button(
            locator="//*[contains(@class, 'sbis_ru-CookieAgreement__close')]",
            name="Кнопка крестик на куках",
            driver=self.driver,
            by=By.XPATH,
        )
