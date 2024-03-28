import allure
from selenium.common import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.elements.utils import WebWait


class BasePage:
    """
    Базовая страницы
    :param driver: Веб драйвер
    """

    def __init__(
        self,
        driver: Remote,
    ) -> None:
        self.driver = driver

    @property
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Перейти на страницу")
    def get(self, url: str) -> "BasePage":
        """Переход на страницу"""
        self.driver.get(url)
        return self

    def clear_session(self) -> None:
        """Очистка сессии, куков, localStorage и обновление страницы"""
        self.driver.execute_script("sessionStorage.clear();")
        self.driver.execute_script("localStorage.clear();")
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def element_is_exist(self, locator: str, raises: bool = False) -> bool:
        """Проверить что эелемент виден на странице"""
        try:
            WebWait(driver=self.driver, timeout=5).until(
                ec.invisibility_of_element((By.ID, locator)),
            )
            return True
        except TimeoutException:
            if raises:
                raise
            return False

    def switch_to_last_tab(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])
