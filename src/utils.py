import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

from src.external_api import currency_convert

# Получение абсолютного пути к директории проекта
project_root = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)
log_file_path = project_root / "logs" / "utils_logfile.log"
file_handler = logging.FileHandler(log_file_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_from_json(path_to_json: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path_to_json, "r") as json_file:
            result = json.load(json_file)
            if not isinstance(result, list):
                logger.error("В JSON должен быть список")
                result = []
            else:
                logger.info("JSON прочитан успешно")
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError) as e:
        logger.error(f"Ошибка чтения JSON: {e}")
        result = []
    return result


def amount_of_transaction(transaction: Dict[str, Any]) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    amount_str: Optional[str] = transaction.get("operationAmount", {}).get("amount", None)
    if amount_str is None:
        logger.error("Сумма не найдена")
        raise Exception("Сумма не найдена")

    try:
        amount = float(amount_str)
    except ValueError as e:
        logger.error(f"Некорректная сумма транзакции: {e}")
        raise ValueError("Некорректная сумма транзакции")

    currency: Optional[str] = transaction.get("operationAmount", {}).get("currency", {}).get("code", None)
    if currency is None:
        logger.error("Валюта не указана")
        raise Exception("Валюта не указана")

    if currency != "RUB":
        try:
            amount = currency_convert(currency, "RUB", amount)
            logger.info(f"Успешная конверсия из {currency} в RUB")
        except Exception as e:
            logger.error(f"Ошибка при конвертации валюты: {e}")
            raise ValueError("Ошибка конвертации валюты")

    return amount
