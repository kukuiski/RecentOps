import csv
import logging
from pathlib import Path
from typing import Any

import pandas as pd

from src.utils import get_transactions_from_json

# Получение абсолютного пути к директории проекта
project_root = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)
log_file_path = project_root / "logs" / "data_loaders_logfile.log"
file_handler = logging.FileHandler(log_file_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_data_from_csv(file_path: str) -> Any:
    """Читает из CSV-файла и возвращает транзакции в виде словаря"""
    result = []
    try:
        with open(file_path) as csv_file:
            result = list(csv.DictReader(csv_file, delimiter=';'))
            if result:
                logger.info(f"Файл {file_path} успешно прочитан")
            else:
                logger.warning(f"Файл {file_path} не содержит данных")
    except (FileNotFoundError, TypeError, ValueError) as e:
        logger.error(f"Ошибка чтения CSV: {e}")
    return result


def read_data_from_excel(file_path: str) -> Any:
    """Читает из Excel-файла и возвращает транзакции в виде словаря"""
    result = []
    try:
        result = pd.read_excel(file_path).to_dict(orient="records")
        if result:
            logger.info(f"Файл {file_path} успешно прочитан")
        else:
            logger.error(f"Файл {file_path} не содержит данных")
    except (FileNotFoundError, TypeError, ValueError) as e:
        logger.error(f"Ошибка чтения Excel: {e}")
    return result


def read_normalized_json(file_path: str) -> Any:
    """Читает JSON-файл и нормализует, приводя индексы в соответствие с CSV"""
    df = pd.json_normalize(get_transactions_from_json(file_path), sep='_')
    df = df.rename(columns={
        'operationAmount_amount': 'amount',
        'operationAmount_currency_name': 'currency_name',
        'operationAmount_currency_code': 'currency_code'
    })
    df = df[['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']]
    return df
