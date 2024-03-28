from selenium.webdriver import Remote

from src.pages.about_page import About
from src.pages.contacts_page import Contacts
from src.pages.cookie_page import Cookie
from src.pages.sbis_page import Sbis
from src.pages.tensor_page import Tensor


def test_1(browser: Remote) -> None:
    # Создание объекта страницы Sbis и открытие в браузере страницы sbis.ru
    sbis_page = Sbis(browser)
    sbis_page.get("https://sbis.ru")

    # Находим и кликаем на кнопку контактов на странице Sbis
    sbis_page.contacts_button.click()

    # Создание объекта страницы Contacts для работы с ней
    contacts_page = Contacts(browser)

    # Клик по кнопке, связанной с компанией Tensor на странице контактов
    contacts_page.tensor_button.click()

    # Переключаемся на последнюю открытую вкладку браузера
    contacts_page.switch_to_last_tab()

    # Следующий шаг - закрытие уведомления о куки на новой странице
    cookie_page = Cookie(browser)
    cookie_page.tensor_cookie_close_button.click()

    # Создание объекта страницы Tensor и выполнение действий на ней
    tensor_page = Tensor(browser)

    # Наведение на кнопку "О компании" и выполнение клика
    tensor_page.about_button.move_and_click()

    # Проверка URL страницы, убеждаемся, что мы находимся на странице О компании
    assert tensor_page.get_current_url == "https://tensor.ru/about"

    # Создание объекта страницы About для выполнения утверждений на ней
    about_page = About(browser)

    # Проверка, что все четыре изображения на странице "О компании" имеют одинаковую ширину
    assert (
        about_page.image_1.get_attribute(value="width")
        == about_page.image_2.get_attribute(value="width")
        == about_page.image_3.get_attribute(value="width")
        == about_page.image_4.get_attribute(value="width")
    )

    # Проверка, что все четыре изображения имеют одинаковую высоту
    assert (
        about_page.image_1.get_attribute(value="height")
        == about_page.image_2.get_attribute(value="height")
        == about_page.image_3.get_attribute(value="height")
        == about_page.image_4.get_attribute(value="height")
    )
