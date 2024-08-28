import masks


def mask_account_card(account_or_card_type_and_number: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """

    result_string = ''

    # Находим первое слово в строке и если оно 'Счет', то обрабатываем как счёт
    list_of_strings = account_or_card_type_and_number.split()
    if list_of_strings[1] == 'Счет':
        result_string = 'Счет ' + masks.get_mask_account(int(list_of_strings[-1]))
    else:
        result_string = " ".join(list_of_strings[:-1]) + masks.get_mask_card_number(int(list_of_strings[-1]))

    return result_string
