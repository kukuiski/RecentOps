import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("number, expected",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")])
def test_mask_account_card_parametrized(number, expected):
    # Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
    assert mask_account_card(number) == expected


def test_mask_account_card():
    # Тестирование правильности маскирования номера карты
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

    # Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum 7000-7922-8960-6361")

    with pytest.raises(ValueError):
        mask_account_card("VisaPlatinum7000792289606361")

    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum 70007922896063611")


def test_get_date():
    # Тестирование правильности преобразования даты.
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    # Проверка работы функции на различных входных форматах даты,
    # включая граничные случаи и нестандартные строки с датами.
    assert get_date("2024-03-11") == "11.03.2024"
    with pytest.raises(ValueError):
        get_date("2024-03-111")
    with pytest.raises(ValueError):
        get_date("2024 03 11")
    with pytest.raises(ValueError):
        get_date("24-03-11")

    # Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
    with pytest.raises(ValueError):
        get_date("")
