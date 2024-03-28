"""Модуль для хранения функций реализующих взаимодействие с allure и тест кейсами"""
from typing import Any

import allure
from allure_commons._allure import StepContext


class StepContextEmpty:
    """Пустой менеджер контекста для степов"""

    def __init__(self, *args, **kwargs) -> None:
        pass

    def __enter__(self) -> None:
        pass

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # noqa: ANN001
        pass


def _parameters(**kwargs) -> dict[str, str]:
    """Приводит все аргументы к строке"""
    return {str(key): str(value) for key, value in kwargs.items()}


def step(
    _title: str | None,
    _params: dict[Any, Any] | None = None,
    _empty: bool = False,
    **kwargs,
) -> StepContext | StepContextEmpty:
    """
    Менеджер контекста для степа
    :param _title: Название степа
    :param _params: Параметры передаваемые в степ
    :param _empty: Пустой степ не попадает в allure
    :param kwargs: Именовынные параметры передаваемые в степ
    """
    if _empty or _title is None:
        return StepContextEmpty()
    _params = _params or {}
    _params.update(**kwargs)
    params = _parameters(**_params)
    return StepContext(title=_title, params=params)


def case(*, case_id: int, title: str) -> Any:  # pylint: disable=redefined-builtin
    """
    Декоратор для интеграции c Allure
    :param case_id: ID Тест кейса
    :param title: Название тест кейса
    """

    def _wrap(func: Any) -> Any:
        func = allure.id(str(case_id))(func)
        func = allure.title(title)(func)
        if func.__doc__:
            func = allure.description(func.__doc__)(func)
        return func

    return _wrap


__all__ = ["case", "step"]
