def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    # Приводим номер карты к строковому типу
    card_number_str = str(card_number)

    # Формируем маску
    masked_card_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"

    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    # Приводим номер счёта к строковому типу
    account_number_str = str(account_number)

    # Формируем маску
    masked_account_number = f"**{account_number_str[-4:]}"

    return masked_account_number
