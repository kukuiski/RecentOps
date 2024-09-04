import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(valid_card_numbers, invalid_card_numbers):
    # Тестирование правильности маскирования номера карты
    for card_number, masked_card in valid_card_numbers:
        assert get_mask_card_number(card_number) == masked_card

    # Тестирование на различных входных форматах номеров карт
    for invalid_card in invalid_card_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_card)


def test_get_mask_account(valid_account_numbers, invalid_account_numbers):
    # Тестирование правильности маскирования номера счета
    for account_number, masked_account in valid_account_numbers:
        assert get_mask_account(account_number) == masked_account

    # Тестирование на различных входных форматах номеров счетов
    for invalid_account in invalid_account_numbers:
        with pytest.raises(ValueError):
            get_mask_account(invalid_account)
