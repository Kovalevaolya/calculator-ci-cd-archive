"""Простой калькулятор для демонстрации CI/CD."""


def add(first: float, second: float) -> float:
    """Возвращает сумму двух чисел."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Возвращает разность двух чисел."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Возвращает произведение двух чисел."""
    return first * second


def divide(first: float, second: float) -> float:
    """Возвращает частное двух чисел."""
    if second == 0:
        raise ValueError("Деление на ноль невозможно")
    return first / second
