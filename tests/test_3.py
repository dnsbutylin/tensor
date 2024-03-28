from selenium.webdriver import Remote

from src.pages.cookie_page import Cookie
from src.pages.sbis_page import Sbis


def test_3(browser: Remote) -> None:
    sbis_page = Sbis(browser)
    sbis_page.get("https://sbis.ru")
    cookie_page = Cookie(browser)
    cookie_page.sbis_cookie_close_button.click()
    # TODO нет кнопки "Скачать сбис" нужно править ТЗ
