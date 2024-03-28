from selenium.webdriver.common.by import By

from ..elements.base_element import Button, Text
from .base_page import BasePage


class Contacts(BasePage):
    @property
    def tensor_button(self) -> Button:
        return Button(
            locator="//a[@class='sbisru-Contacts__logo-tensor mb-12']/img",
            name="Тензор",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def region_button(self) -> Button:
        return Button(
            locator="//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']/span",
            name="Область",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def region_text(self) -> Text:
        return Text(
            locator="//div[@id='city-id-2']",
            name="Город",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def yaroslavl_partner_text(self) -> Text:
        return Text(
            locator="//*[text()='СБИС - Ярославль']",
            name="Партнер",
            driver=self.driver,
            by=By.XPATH,
        )

    @property
    def kamchatka_partner_text(self) -> Text:
        return Text(
            locator="//*[text()='СБИС - Камчатка']",
            name="Партнер",
            driver=self.driver,
            by=By.XPATH,
        )
