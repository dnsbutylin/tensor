from selenium.webdriver import Remote

from src.pages.contacts_page import Contacts
from src.pages.cookie_page import Cookie
from src.pages.sbis_page import Sbis
from src.pages.region_pop_up_page import RegionPopUp


def test_2(browser: Remote) -> None:
    # Создаём объект страницы Sbis
    sbis_page = Sbis(browser)
    # Заходим на главную страницу Sbis.
    sbis_page.get("https://sbis.ru")
    # Кликаем по кнопке для перехода на страницу контактов.
    sbis_page.contacts_button.click()

    # Создаём объект страницы Cookie
    cookie_page = Cookie(browser)
    # Закрываем всплывающее уведомление о куках на странице sbis.
    cookie_page.sbis_cookie_close_button.click()

    # Переходим к работе со страницей контактов
    contact_page = Contacts(browser)
    # Проверяем, что текст с регионом на странице контактов совпадает с "Ярославль".
    assert contact_page.region_text.text() == "Ярославль"
    # Убеждаемся, что кнопка с регионом отображает текст "Ярославская обл.".
    assert contact_page.region_button.text() == "Ярославская обл."
    # Проверяем, что текст на странице контактов корректно указывает на партнёра в Ярославле.
    assert contact_page.yaroslavl_partner_text.text() == "СБИС - Ярославль"

    # Нажимаем на кнопку с регионом для вызова всплывающего окна с выбором региона.
    contact_page.region_button.click()

    # Создаём объект всплывающего окна, чтобы выбрать другой регион.
    region_pop_up = RegionPopUp(browser)
    # В окне выбора региона нажимаем на кнопку для перехода к Камчатскому краю.
    region_pop_up.kamchatka_button.click()

    # Проверяем наличие элемента кнопки региона после изменения региона.
    contact_page.element_is_exist(contact_page.region_button.locator)
    # Проверяем, что текст с текущим регионом теперь отображает "Петропавловск-Камчатский".
    assert contact_page.region_text.text() == "Петропавловск-Камчатский"
    # Убедимся, что кнопка с регионом теперь показывает "Камчатский край". Это подтверждает успешную смену региона.
    assert contact_page.region_button.text() == "Камчатский край"
    # Наконец, проверяем, что текст на странице корректно обновился, указывая на партнёра в Камчатском крае.
    assert contact_page.kamchatka_partner_text.text() == "СБИС - Камчатка"
