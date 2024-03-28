from selenium.webdriver.support.ui import WebDriverWait


class WebWait(WebDriverWait):
    """Переопределение ожидания, для возможности ожидания от элемента"""

    def __repr__(self) -> str:
        return f"<{self.__class__.__module__}.{self.__class__.__name__}>"
