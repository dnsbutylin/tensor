from selenium.webdriver import Remote

from src.pages.about_page import About
from src.pages.contacts_page import Contacts
from src.pages.cookie_page import Cookie
from src.pages.sbis_page import Sbis
from src.pages.tensor_page import Tensor


def test_1(browser: Remote) -> None:
    sbis_page = Sbis(browser)
    sbis_page.get("https://sbis.ru")
    sbis_page.contacts_button.click()

    contacts_page = Contacts(browser)
    contacts_page.tensor_button.click()
    contacts_page.switch_to_last_tab()

    cookie_page = Cookie(browser)
    cookie_page.tensor_cookie_close_button.click()

    tensor_page = Tensor(browser)
    tensor_page.about_button.move_and_click()
    assert tensor_page.get_current_url == "https://tensor.ru/about"
    about_page = About(browser)

    assert (
        about_page.image_1.get_attribute(value="width")
        == about_page.image_2.get_attribute(value="width")
        == about_page.image_3.get_attribute(value="width")
        == about_page.image_4.get_attribute(value="width")
    )
    assert (
        about_page.image_1.get_attribute(value="height")
        == about_page.image_2.get_attribute(value="height")
        == about_page.image_3.get_attribute(value="height")
        == about_page.image_4.get_attribute(value="height")
    )

