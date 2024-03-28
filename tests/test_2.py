from selenium.webdriver import Remote

from src.pages.contacts_page import Contacts
from src.pages.cookie_page import Cookie
from src.pages.sbis_page import Sbis
from src.pages.region_pop_up_page import RegionPopUp


def test_2(browser: Remote) -> None:
    sbis_page = Sbis(browser)
    sbis_page.get("https://sbis.ru")
    sbis_page.contacts_button.click()

    cookie_page = Cookie(browser)
    cookie_page.sbis_cookie_close_button.click()

    contact_page = Contacts(browser)
    assert contact_page.region_text.text() == "Ярославль"
    assert contact_page.region_button.text() == "Ярославская обл."
    assert contact_page.yaroslavl_partner_text.text() == "СБИС - Ярославль"

    contact_page.region_button.click()

    region_pop_up = RegionPopUp(browser)
    region_pop_up.kamchatka_button.click()

    contact_page.element_is_exist(contact_page.region_button.locator)
    assert contact_page.region_text.text() == "Петропавловск-Камчатский"
    assert contact_page.region_button.text() == "Камчатский край"
    assert contact_page.kamchatka_partner_text.text() == "СБИС - Камчатка"
