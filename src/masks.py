import logging

# Настройка логгера
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks_logfile.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    try:
        # Проверяем нулевую строку номера
        if len(card_number) == 0:
            raise ValueError("Номер карты отсутствует")

        # Проверяем на условие «все цифры»
        if not card_number.isdigit():
            raise ValueError("Номер карты должен состоять только из цифр")

        # Проверяем длину номера карты
        if len(card_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")

        # Формируем маску
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.info("Маска карты сформирована")
        return masked_card_number

    except ValueError as e:
        logger.error(f"Ошибка при формировании маски карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""

    try:
        # Проверяем нулевую строку номера
        if len(account_number) == 0:
            raise ValueError("Номер счета отсутствует")

        # Проверяем на условие «все цифры»
        if not account_number.isdigit():
            raise ValueError("Номер счета должен состоять только из цифр")

        # Проверяем длину номера счета
        if len(account_number) != 20:
            raise ValueError("Номер счета должен содержать 20 цифр")

        # Формируем маску
        masked_account_number = f"**{account_number[-4:]}"
        logger.info("Маска счета сформирована")
        return masked_account_number

    except ValueError as e:
        logger.error(f"Ошибка при формировании маски карты: {e}")
        raise
