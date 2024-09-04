import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Тестирование правильности маскирования номера карты
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Тестирование на различных входных форматах номеров карт

    # Номер длиной меньше 16 символов
    with pytest.raises(ValueError):
        get_mask_card_number("123456789012")  # Длина 12 символов

    # Номер длиной больше 16 символов
    with pytest.raises(ValueError):
        get_mask_card_number("12345678901234567890")  # Длина 20 символов

    # Номер содержит символы, отличные от цифры
    with pytest.raises(ValueError):
        get_mask_card_number("1234-5678-9012-3456")

    # Номер отсутствует
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_account():
    # Тестирование правильности маскирования номера карты
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("12345678901234562439") == "**2439"

    # Тестирование на различных входных форматах номеров карт

    # Номер длиной меньше 20 символов
    with pytest.raises(ValueError):
        get_mask_account("1234567890123456243")  # Длина 19 символов

    # Номер длиной больше 20 символов
    with pytest.raises(ValueError):
        get_mask_account("123456789012345624391")  # Длина 21 символов

    # Номер отсутствует
    with pytest.raises(ValueError):
        get_mask_account("")

    # Номер содержит символы, отличные от цифры
    with pytest.raises(ValueError):
        get_mask_account("#12345678901234562439")

