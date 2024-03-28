import json
import logging
from pathlib import Path
from typing import Any, Final, Iterator

import allure
from _pytest.tmpdir import TempPathFactory
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver import Remote

log = logging.getLogger("pytest")
CACHE: Final[dict[str, Any]] = {}


def screenshot(driver: webdriver.Remote, node_name: str | None = None) -> None:
    """
    Делает скрин и формирует ссылку на видео прогона
    :param driver: Экземпляр вебдрайвера
    :param node_name: Имя pytest ноды (optional)
    :param report: pytest репорт теста (optional)
    """

    if not getattr(driver, "is_stop", False):
        node_name = node_name or "Screenshot"
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=node_name,
                attachment_type=AttachmentType.PNG,
            )
        except Exception as err:
            log.error(f"Fail screenshot: {err}")


def save_browser_log(driver: webdriver.Remote) -> None:
    """Пытается вытащить логи браузера"""
    try:
        browser_logs = driver.get_log("browser")
        if "browser" in driver.log_types and browser_logs:
            allure.attach(
                json.dumps(browser_logs, indent=4, ensure_ascii=False),
                name="browser_log.json",
                attachment_type=AttachmentType.JSON,
            )
    except Exception as err:
        log.error(f"Fail get browser log: {err}")


@pytest.fixture(scope="session")
def root_path() -> Path:
    """Путь до корня проекта"""
    return Path(__file__).parent.absolute()


@pytest.fixture(scope="session")
def browser_tools_dir(root_path: Path) -> Path:
    """Путь к папке browser_tools"""
    return root_path.joinpath("browser_tools")


def driver_path(browser_tools_dir: Path) -> Path:
    """Путь к бинарнику chromedriver"""
    for driver in browser_tools_dir.glob("chromedriver*"):
        return driver
    raise FileNotFoundError("Не найден бинарник chromedriver")


@pytest.fixture(scope="module", name="tmp")
def temp_folder(tmp_path_factory: TempPathFactory) -> Path:
    """Создание временной директории"""
    tmp_dir = tmp_path_factory.mktemp("tmp_folder")
    pytest._run_tmp_dir = tmp_dir
    return Path(tmp_dir)


class Driver:
    """Создание драйвера"""

    def webdriver(
        self,
        tmp_download: Path,
        browser_tools_dir: Path,
    ) -> Remote:
        """Локальный драйвер"""

        prefs = {"download.default_directory": str(tmp_download)}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(
            executable_path=str(driver_path(browser_tools_dir)),
            options=options,
        )
        return driver


@pytest.fixture(scope="module")
def browser(
    browser_tools_dir: Path,
    tmp: Path,
) -> Iterator[webdriver.Chrome]:
    """Запуск браузера для тестов"""
    tmp_download = tmp / "browser_download"
    if not tmp_download.exists():
        tmp_download.mkdir(parents=True)

    tmp_files = tmp / "browser_files"
    if not tmp_files.exists():
        tmp_files.mkdir(parents=True)

    driver = Driver().webdriver(
        tmp_download=tmp_download,
        browser_tools_dir=browser_tools_dir,
    )
    driver.tmp_download = tmp_download  # type: ignore
    driver.tmp_files = tmp_files  # type: ignore
    driver.maximize_window()
    yield driver
    for i in tmp_download.iterdir():
        i.unlink(missing_ok=True)
    driver.quit()
