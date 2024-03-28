from time import sleep, time
from typing import Any, Callable

NUMBER = int | float


class WaitTimeoutError(Exception):
    """Класс ошибок для wait"""


def wait_for_condition(
    func: Callable,
    *conditions,
    timeout: NUMBER = 30,
    interval: NUMBER = 0.5,
    err_msg: str | None = None,
) -> Any:
    """
    Функция ожидания с валидацией ответа
    :param func: Функция значение которой нужно валидировать
    :param conditions: Функции которые принимают результат выполнения func для проверки
                        (принимает любое кол-во функций)
    :param timeout: Максимальное время ожидания
    :param interval: интервал проверок
    :param err_msg: Сообщение об ошибке
    :return: Результат работы func
    """
    _exc = None
    raise_time = time() + timeout
    while time() < raise_time:
        try:
            result = func()
            if all(check(result) for check in conditions):
                return result
        except Exception as ex:  # pylint: disable=broad-except
            _exc = ex
        sleep(interval)
    exception = _exc or WaitTimeoutError(err_msg or "Wait time out")
    raise exception
