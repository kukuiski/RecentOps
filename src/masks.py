def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    # Проверяем нулевую строку номера
    if len(card_number) == 0:
        raise ValueError("Номер карты отсутствует")

    # Проверяем на условие «все цифры»
    if not card_number.isdigit():
        raise ValueError("Номер должен состоять только из цифр")

    # Проверяем длину номера карты
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Формируем маску
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    # 73654108430135874305 – входной аргумент.
    # **4305 – выход функции.

    # Проверяем нулевую строку номера
    if len(account_number) == 0:
        raise ValueError("Номер счёта отсутствует")

    # Проверяем на условие «все цифры»
    if not account_number.isdigit():
        raise ValueError("Номер должен состоять только из цифр")

    # Проверяем длину номера карты
    if len(account_number) != 20:
        raise ValueError("Номер должен содержать 20 цифр")

    # Формируем маску
    masked_account_number = f"**{account_number[-4:]}"

    return masked_account_number
